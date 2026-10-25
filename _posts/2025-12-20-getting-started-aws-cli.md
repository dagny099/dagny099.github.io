---
layout: post
title: "The Data Scientist's Toolkit: Launch an RDS Database with the AWS CLI"
subtitle: "How I gave fourteen years of workout data a home in the cloud, one repeatable command at a time"
date: 2025-12-20
last_modified_at: 2026-10-25
permalink: /blog/aws-cli-tutorial-launch-rds-for-ec2-access/
header:
  teaser: /assets/diagrams/aws-cli-rds-network-v1.svg
excerpt: "A step-by-step guide to standing up a private MySQL database on Amazon RDS entirely from the command line: SSO credentials, a subnet group, a security group that trusts only your app server, the database itself, an encrypted connection to prove it works, and the commands to tear it all down."
excerpt_display: true
tags: [aws, aws-cli, rds, mysql, data-engineering, cloud, tutorial]
stack: [AWS CLI, AWS RDS, MySQL, IAM Identity Center, EC2]
classes: wide
categories: [tutorial]
pagination:
  enabled: true
---

*Updated October 2026. Every command and `--query` below was re-run against AWS CLI 2.38 using a local AWS emulator (moto), in both bash and zsh, and the sign-in prompts were checked against the real CLI. This version also adds the connection test and cleanup steps the first one was missing.*

My fitness dashboard started as a pile of CSV exports: fourteen years of MapMyRun history, 2,593 workouts, and a Date column that couldn't settle on a format.

{% include figure image_path="/assets/images/mapmyrun-export-raw.png" alt="Spreadsheet of a raw MapMyRun workout export. The Date Submitted column switches from values like 9-Mar-25 to values like Feb. 28, 2025 partway down. Every row is labeled Run, one row shows a pace of 119.874 minutes per mile, and another row is all zeros." caption="A raw MapMyRun export. The dates change format partway down the same column, one “run” clocks a 120-minute mile, and one row is all zeros." %}

To get from that to a dashboard I could open from anywhere, the data needed a real home: a MySQL database that my Streamlit app on EC2 could query, and that nothing else on the internet could reach. So I gave it one, an Amazon RDS instance named `sweat-db`, and I built it from the command line instead of clicking through the AWS console.

The reason is repeatability. Try remembering all seventeen clicks you made in the console six months from now. A command is something you can re-run, read, paste into a script, and diff. It's also the foundation for infrastructure-as-code later, if you ever want it.

## What we're building

{% include figure image_path="/assets/diagrams/aws-cli-rds-network-v1.svg" alt="Network diagram. Your laptop sends aws CLI commands to the AWS API, which creates resources in the default VPC in us-east-1. The VPC has two default subnets in two availability zones, grouped by Step 5 into the DB subnet group sweat-db-subnets. An EC2 instance running the fitness dashboard sits in one subnet. The RDS MySQL instance sweat-db, created in Step 7 and not publicly accessible, sits inside the security group sweat-db-sg from Step 6. A teal arrow shows TCP 3306 allowed from the EC2 instance's security group. Your laptop reaches the EC2 instance over ssh on port 22. A blocked marker shows there is no public route from the internet to the database." %}

The idea that makes this secure fits in one rule: the database accepts connections on MySQL's port, 3306, only from machines in the app server's security group. Your laptop never talks to the database directly. It talks to the AWS API to build things, and it reaches the app server over SSH.

## Before you start

- **An AWS account** where you can use IAM Identity Center.
- **An EC2 instance** running in your region's default VPC, which you can SSH into. This is the app server. Launching one is outside the scope of this post.
- **The AWS CLI, version 2**, on your laptop.

On macOS, `brew install awscli` installs version 2. On Linux, use AWS's installer:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version    # should print aws-cli/2.x
```

The first version of this post said `pip install awscli`, which installs version 1, the one AWS no longer recommends. It also broke my own rule from the [Poetry post](/blog/poetry-of-python/): the CLI is a tool, so it belongs on your machine, not inside a project's environment.

## Step 1: Make a sign-in that isn't your root account

Your AWS root account has the keys to the entire kingdom, so it shouldn't be what you use day to day. Instead, create a user with just the access you need through **IAM Identity Center**, in the AWS console:

1. Open **IAM Identity Center** and enable it if it isn't already. The console walks you through it.
2. Under **Users**, choose **Add user** and create one for yourself. You'll get an email to set the password.
3. Under **Permission sets**, choose **Create permission set**, pick **Predefined permission set**, and select **AdministratorAccess**. In a real project you'd write a narrower policy with only the permissions you need (the principle of least privilege), but this keeps the tutorial moving.
4. Under **AWS accounts**, check your account, choose **Assign users or groups**, select your user, then the **AdministratorAccess** permission set, and submit.

While you're there, copy the **AWS access portal URL** from the Identity Center dashboard. It looks like `https://d-xxxxxxxxxx.awsapps.com/start`, and you'll need it next.

## Step 2: Connect your terminal with SSO

Instead of long-lived access keys sitting in a file, the CLI can borrow short-lived credentials through Identity Center's single sign-on:

```bash
aws configure sso
```

It asks four questions:

```text
SSO session name (Recommended): sweat
SSO start URL [None]: https://d-xxxxxxxxxx.awsapps.com/start
SSO region [None]: us-east-1
SSO registration scopes [sso:account:access]:
```

The session name is any label you like. The start URL is the portal URL from Step 1, the region is where Identity Center lives, and you can accept the default scope by pressing Enter. Your browser then opens and asks you to approve the sign-in. Back in the terminal, pick your account and the **AdministratorAccess** role, choose a default region and output format, and give the profile a name you'll recognize. I'll use `sweat-admin`.

Then tell every command that follows to use that profile:

```bash
export AWS_PROFILE=sweat-admin
export AWS_PAGER=""
```

The first line fixes a bug in my first version, where only one command carried `--profile`. Every command after it would have quietly used your *default* profile instead, or failed if you don't have one. The second stops the CLI from opening long output in a pager, so a big response doesn't leave your terminal waiting for you to press `q`. When your session expires later, `aws sso login` gets you a fresh one.

## Step 3: "Hello, AWS. Who am I?"

Before building anything, check that the line to AWS works:

```bash
aws sts get-caller-identity
```

AWS should reply with a small JSON object identifying you:

```json
{
    "UserId": "AROAXXXXXXXXXXXX:your-user-name",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/AWSReservedSSO_AdministratorAccess_xxxx/your-user-name"
}
```

Seeing that means you're ready to build.

## Step 4: Find your network

The database needs to live inside a network. We'll use the default VPC (Virtual Private Cloud) that every region comes with, and two of its subnets:

```bash
VPC_ID=$(aws ec2 describe-vpcs \
    --filters "Name=isDefault,Values=true" \
    --query "Vpcs[0].VpcId" --output text)

SUBNET_IDS=$(aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=$VPC_ID" \
    --query "Subnets[0:2].SubnetId" --output json)

echo "VPC: $VPC_ID"
aws ec2 describe-subnets --subnet-ids "$SUBNET_IDS" \
    --query "Subnets[].[SubnetId,AvailabilityZone]" --output text
```

The last command should print two subnet IDs in two different Availability Zones, like `us-east-1a` and `us-east-1b`. RDS requires that: if one zone has a bad day, the database can live in the other. A default VPC has one subnet per zone, so the first two are always in different zones.

Notice `--output json` and the quotes around `"$SUBNET_IDS"`. The first version of this post used plain text output and an unquoted variable, which works in bash but fails in zsh, the default shell on a Mac. zsh hands both IDs to AWS as a single string, and AWS answers that subnet `subnet-aaa subnet-bbb` doesn't exist. A JSON list in quotes works in both shells.

## Step 5: Create the DB subnet group

A DB subnet group is a short list of subnets where RDS is allowed to put your database. Think of it as giving the database the zip codes it may live in:

```bash
aws rds create-db-subnet-group \
    --db-subnet-group-name sweat-db-subnets \
    --db-subnet-group-description "Subnets for sweat-db" \
    --subnet-ids "$SUBNET_IDS"
```

## Step 6: Build the firewall

A security group is a virtual firewall, and a new one denies all incoming traffic. We'll create one for the database, then open exactly one door in it: MySQL's port, from the app server.

```bash
DB_SG_ID=$(aws ec2 create-security-group \
    --group-name sweat-db-sg \
    --description "MySQL access to sweat-db from my EC2 instance" \
    --vpc-id "$VPC_ID" \
    --query "GroupId" --output text)

EC2_INSTANCE_ID=i-0123456789abcdef0    # your app server's instance ID

EC2_SG_ID=$(aws ec2 describe-instances \
    --instance-ids "$EC2_INSTANCE_ID" \
    --query "Reservations[0].Instances[0].SecurityGroups[0].GroupId" --output text)

echo "App server's security group: $EC2_SG_ID"
```

If that prints `None`, or an error, fix it before going on. Otherwise the next command fails with a confusing message about a security group named `None`.

```bash
aws ec2 authorize-security-group-ingress \
    --group-id "$DB_SG_ID" \
    --protocol tcp \
    --port 3306 \
    --source-group "$EC2_SG_ID"
```

The rule's source is a *security group*, not an IP address. Any instance in the app server's group can connect, nothing else can, and the rule keeps working if the server's IP address changes. One caution: if your EC2 instance uses the VPC's *default* security group, every other instance in that group gets access too. Giving the app server its own security group keeps the door narrow.

## Step 7: Create the database

This is the main event. The command is long, but it only assembles the pieces from the last three steps. First, type the master password without it landing in your shell history:

```bash
printf 'Master password: '; read -s DB_PASSWORD; echo
```

RDS wants 8 to 41 characters, with no spaces and none of `/`, `"`, or `@`. Then create the instance:

```bash
aws rds create-db-instance \
    --db-instance-identifier sweat-db \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --allocated-storage 20 \
    --master-username sweatadmin \
    --master-user-password "$DB_PASSWORD" \
    --vpc-security-group-ids "$DB_SG_ID" \
    --db-subnet-group-name sweat-db-subnets \
    --no-publicly-accessible
```

A few of these are worth a word:

- `--db-instance-identifier sweat-db` names the server. The database *inside* it, `sweat`, is something you'll create in Step 9.
- `--no-publicly-accessible` means the database gets no public address. That's the blocked arrow in the diagram.
- `db.t3.micro` is one of the smallest instance classes. Whether it's covered by the Free Tier depends on your account's age: accounts opened after July 15, 2025 get a credit-based free plan instead of the old monthly hours, so check the [Free Tier page](https://aws.amazon.com/free/) before you leave it running.

## Step 8: Wait for it, then get the endpoint

Provisioning takes several minutes. Instead of checking every minute by hand, let the CLI wait for you:

```bash
aws rds wait db-instance-available --db-instance-identifier sweat-db
```

It returns when the database is ready. (If it times out, just run it again.) Then ask for the address your app will connect to, called the **endpoint**:

```bash
DB_ENDPOINT=$(aws rds describe-db-instances \
    --db-instance-identifier sweat-db \
    --query "DBInstances[0].Endpoint.Address" --output text)

echo "$DB_ENDPOINT"
```

You'll get something like `sweat-db.abc123xyz.us-east-1.rds.amazonaws.com`. Copy it; you'll paste it on the app server.

## Step 9: Prove it works from the app server

The database can't be reached from your laptop, by design, so the test happens on the EC2 instance. SSH in:

```bash
ssh -i ~/.ssh/your-key.pem ec2-user@your-ec2-public-dns
```

On the instance (Amazon Linux 2023), install a MySQL client and download the certificate bundle AWS publishes for RDS:

```bash
sudo dnf install -y mariadb105
curl -O https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

`mariadb105` is the MySQL-compatible client that Amazon Linux 2023 provides. On Ubuntu, `sudo apt install mariadb-client` gives you the same client and flags. Now connect, pasting your endpoint after `-h`:

```bash
mysql -h sweat-db.abc123xyz.us-east-1.rds.amazonaws.com -P 3306 -u sweatadmin -p \
    --ssl-ca=global-bundle.pem --ssl-verify-server-cert
```

The two `--ssl` flags encrypt the connection and check that you're really talking to your RDS instance. RDS for MySQL doesn't require encryption by default, so without them you'd likely still connect, just in plain text.

Once you're at the `MariaDB [(none)]>` prompt, create the database and check the connection:

```sql
CREATE DATABASE sweat;
SHOW DATABASES;
SHOW STATUS LIKE 'Ssl_cipher';
```

If `sweat` appears in the list and `Ssl_cipher` shows a value (something like `TLS_AES_256_GCM_SHA384`), you have an encrypted connection from the app server to its own private database. An empty `Ssl_cipher` means the connection isn't encrypted.

From here, the endpoint, user, and password go into your app's configuration. In my dashboard, a config switch pointed development at a local MySQL and production at this endpoint. Keeping the password in a `.env` file, as in the [Poetry post](/blog/poetry-of-python/#step-5-keep-secrets-in-env-out-of-git), keeps it out of Git.

## When you're done: clean up

An RDS instance bills for every hour it exists, whether or not anything queries it. Stopping it pauses the instance charges, but AWS automatically starts a stopped instance again after seven days. If you're finished with it, delete it, along with the pieces you built around it:

```bash
aws rds delete-db-instance \
    --db-instance-identifier sweat-db \
    --final-db-snapshot-identifier sweat-db-final

aws rds wait db-instance-deleted --db-instance-identifier sweat-db
aws rds delete-db-subnet-group --db-subnet-group-name sweat-db-subnets
aws ec2 delete-security-group --group-id "$DB_SG_ID"
```

The final snapshot keeps a copy of your data that you can restore later, for a small storage charge. If the data doesn't matter, use `--skip-final-snapshot` instead.

## Why the command line was worth it

The console would have gotten me a database faster the first time. The commands get me the same database every time, and they double as documentation. Six months from now, this page is how I'll remember what I built and why port 3306 only answers one server.

Previously in the Data Scientist's Toolkit: [Poetry + direnv for project isolation](/blog/poetry-of-python/).

## Resources

- [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Configuring IAM Identity Center authentication with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
- [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)
