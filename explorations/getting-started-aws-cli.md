---
title: "From Analyst to Architect: A Data Scientist's Guide to Launching an RDS Database with the AWS CLI"
description: "Level up your data skills by moving beyond jupyter notebooks. Learn how to build robust, repeatable data infrastructure using the tools of modern data engineering."
header:
  overlay_image: /assets/images/blog/aws-cli-banner.jpg
  overlay_filter: 0.5
  caption: "Photo by Anders Jensen on Unsplash"
permalink: /explorations/aws-cli-tutorial-launch-rds-for-ec2-access/
layout: single
section: explorations
tags: [aws, data engineering, cli, rds, python, tutorial,]
---

# A Step-by-Step Guide to Launching an RDS Database with the AWS CLI

*This is a part of The Data Scientist's CLI Handbook, currently being re-organized and posted. Stay tuned for updates to this series, Late July 2025*

As data scientists, we're masters of our domain. We crunch numbers, build models, and turn raw data into compelling narratives. But what happens when your model is ready for production? Where does the data come from, and where does it live?

More and more, the line between data science and data engineering is blurring. To truly own the entire data lifecycle, you need to speak the language of the cloud. Today, we’re going to do just that. We’ll ditch the GUI and embrace the command line to spin up our very own AWS RDS (Relational Database Service) database.

Why bother? Because building infrastructure via the CLI (Command Line Interface) is:

- **Repeatable**: Try remembering all 17 clicks you made in the AWS Console. With a script, you can do it in milliseconds, every time, exactly the same.
- **Automatable**: This is the foundation of CI/CD (Continuous Integration/Deployment) and infrastructure-as-code (IaC).
- **Flexible**: You gain fine-grained control over resources that GUIs sometimes hide.

This isn’t just an academic exercise; it’s a career superpower. Grab your coffee and let’s build something.

*Visual Suggestion: A stylized, graphical representation of a data pipeline flow, showing an EC2 instance connecting to an RDS database, which in turn feeds a web application.*

---

### Pre-Req: Install the AWS CLI

The AWS CLI is a Python application, so the simplest way to get it is with `pip` or `poetry`.

```bash
# Using pip
pip install awscli

# Or for Poetry users:
poetry add awscli
````

-----

### Step 1: The Golden Rule: Don't Use Your Root Account\!

First things first: your AWS root account has the keys to the entire kingdom. We never use it for everyday tasks. Instead, we'll create a dedicated user with specific permissions. The modern, secure way to do this is with **IAM Identity Center**.

1.  **Navigate to IAM Identity Center** in your AWS Console.
2.  Go to the **"Users"** section and click **"Add user."** Create a new user with a username and password.
3.  Now, go to **"AWS accounts"** on the left menu. Select your AWS account by checking the box next to it.
4.  Click **"Assign users or groups."**
5.  Select the user you just created and click **"Next."**
6.  On the next screen, select the **Permission Set**. For this tutorial, choose **`AWSAdministratorAccess`**. In a real-world project, you would create a custom policy with only the permissions you absolutely need (the principle of least privilege).
7.  Click **"Next"** and then **"Submit"** to complete the assignment.

*Visual Suggestion: A screenshot of the final "Review and submit" page in the IAM Identity Center assignment process, clearly showing the User, Permission Set, and Account being linked.*

-----

### Step 2: Configuring Your Local Terminal

Forget about static access keys. The modern way to connect your CLI is with temporary credentials through IAM Identity Center's SSO (Single Sign-On) capabilities.

In your terminal (assuming macOS or Linux), run:

```bash
aws configure sso
```

The CLI will ask you for two pieces of information, which you can find in your AWS Access Portal (the URL is on your IAM Identity Center dashboard):

1.  **SSO start URL**: Looks like `https://d-xxxxxxxxxx.awsapps.com/start`
2.  **SSO Region**: The AWS Region where your Identity Center is configured (e.g., `us-east-1`).

Your browser will pop open, asking you to confirm and authorize the device. Once you do, return to your terminal. It will list the accounts and roles you have access to. Select the `AWSAdministratorAccess` role and give your profile a memorable name when prompted (e.g., `baba-geocue-admin`).

-----

### Step 3: "Hello, AWS. Who Am I?" - Testing Your Credentials

Before we build anything, let's make sure our phone line to AWS is working. Run this command, making sure to use the profile name you just configured:

```bash
aws sts get-caller-identity --profile baba-geocue-admin
```

If everything is correct, AWS will reply with a JSON object identifying you. It's like a successful handshake.

```json
{
    "UserId": "AROAXXXXXXXXXXXX:your-user-name",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/AWSReservedSSO_AWSAdministratorAccess_xxxx/your-user-name"
}
```

Seeing this means you're ready to build\!

-----

### Step 4: Setting the Stage: Networking Basics

Our database can't live in a void. It needs to be in a secure network. We'll place it in our Default VPC (Virtual Private Cloud) and tell it which subnets (sections of the network) it can use.

These commands will find your default network info and save it to shell variables for easy use.

```bash
# Get your default VPC ID
VPC_ID=$(aws ec2 describe-vpcs --filters "Name=isDefault,Values=true" --query "Vpcs[0].VpcId" --output text)

# Get at least two subnet IDs from that VPC
SUBNET_IDS=$(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$VPC_ID" --query "Subnets[0:2].SubnetId" --output text)

echo "Using VPC ID: $VPC_ID"
echo "Using Subnet IDs: $SUBNET_IDS"
```

-----

### Step 5: Creating the DB Subnet Group

A Subnet Group is a simple list of subnets that you tell RDS it's allowed to place a database in. It's like assigning a zip code to your database.

```bash
aws rds create-db-subnet-group \
    --db-subnet-group-name "my-rds-subnet-group" \
    --db-subnet-group-description "Subnet group for my RDS instance" \
    --subnet-ids $SUBNET_IDS
```

-----

### Step 6: Building the Firewall: Security Groups

This is a critical security step. A Security Group is a virtual firewall that, by default, denies all incoming traffic. We need to create one for our database and then add a specific rule to allow our EC2 instance to talk to it.

```bash
# Create the security group for the database
DB_SG_ID=$(aws ec2 create-security-group --group-name "rds-db-sg" --description "Security group for RDS DB" --vpc-id $VPC_ID --query "GroupId" --output text)

# Get your EC2 instance's security group ID (assuming you have one running)
# Note: You'd need to adjust the query if you have multiple instances
EC2_SG_ID=$(aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[0].Instances[0].SecurityGroups[0].GroupId" --output text)

# Add a rule to allow inbound traffic from the EC2 instance on the MySQL port (3306)
aws ec2 authorize-security-group-ingress \
    --group-id $DB_SG_ID \
    --protocol tcp \
    --port 3306 \
    --source-group $EC2_SG_ID
```

This is much more secure than opening the port to the entire internet\!

*Visual Suggestion: A simple network diagram showing two boxes labeled "EC2 Security Group" and "RDS Security Group." An arrow originates from the EC2 box, points to the RDS box, and is labeled "Allow traffic on Port 3306."*

-----

### Step 7: Showtime\! Creating the RDS Instance

This is the main event. The command is long, but it just puts together all the pieces we've defined. We're creating a small, Free Tier-eligible MySQL database.

```bash
aws rds create-db-instance \
    --db-instance-identifier "sweat-db" \
    --db-instance-class "db.t3.micro" \
    --engine "mysql" \
    --allocated-storage 20 \
    --master-username "sweatadmin" \
    --master-user-password "a-very-strong-and-secure-password" \
    --vpc-security-group-ids $DB_SG_ID \
    --db-subnet-group-name "my-rds-subnet-group" \
    --no-publicly-accessible
```

**Remember:** Choose a *very* strong password. The `--db-instance-identifier` (`sweat-db`) is the name of the server resource, not the logical database you'll create inside it (`sweat`).

-----

### Step 8: Are We There Yet? Checking the Status

Provisioning the database takes a few minutes. You can grab another cup of coffee and check on its progress with this command:

```bash
aws rds describe-db-instances --db-instance-identifier "sweat-db" --query "DBInstances[0].DBInstanceStatus"
```

Run it every minute or so. Once the status changes from `creating` to `available`, your database is live\!

Now, get the connection string, which we call the **Endpoint**:

```bash
aws rds describe-db-instances --db-instance-identifier "sweat-db" --query "DBInstances[0].Endpoint.Address" --output text
```

You'll get back something like: `sweat-db.random-chars.us-east-1.rds.amazonaws.com`.

-----

### Conclusion and What's Next

Congratulations\! You've just provisioned a secure, cloud-native database entirely from the command line. You didn't just click buttons; you defined resources, configured networking, and secured access like a true data engineer.

The next step is to prove it works. In a follow-up post, we'll SSH into our EC2 instance, install a MySQL client, and use the endpoint you just retrieved to connect to our new database. Stay tuned\!
