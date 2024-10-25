# Git Workflow for Keeping Organized

This workflow keeps my production branch (`main`) clean while allowing continuous development on `dev_branch`, with further experimentation through feature branches.


## 1. Main Branch Setup
* **`main` branch**: This will represent the stable production-ready code that gets deployed to a remote server (e.g. EC2 instance).

* **`dev_branch`**: This is where we'll develop and test code changes.

## 2. Development Workflow
On both development machines (e.g. laptop and desktop), we'll work on the `dev_branch `and use Git to sync your changes.

Start by checking out `dev_branch`:

```
git checkout dev_branch
```

Pull the latest changes from GitHub to ensure you’re working with the most up-to-date code:

```
git pull origin dev_branch
```

Make your changes locally (on either machine).

Once changes are complete, stage and commit:

```
git add .
git commit -m "Describe your changes"
```

Push the changes to the remote `dev_branch`:

```
git push origin dev_branch
```

## 3. Deployment Workflow
On your EC2 instance, you want to deploy the code from the `main` branch. So, once you’re satisfied with the changes in `dev_branch` and have tested locally:

On your **local machine** (laptop or desktop), merge `dev_branch` into `main`:

```
git checkout main
git pull origin main   # Ensure you have the latest `main` branch code
git merge dev_branch   # Merge your dev work into `main`
```

Push the updated main branch to GitHub:

```
git push origin main
```

On your **EC2 instance**, pull the `main` branch from GitHub:

```
git checkout main
git pull origin main
```

Deploy the updated code on your EC2 instance. Depending on your setup, you may need to restart the application or reload services.

## 4. Feature Branches (Optional)
If you are working on larger features or experiments, you might want to create feature branches off of `dev_branch`, and later merge those into `dev_branch` before merging into main:

```
git checkout -b feature_branch_name dev_branch
```

Once done, merge the feature branch back into `dev_branch`:

```
git checkout dev_branch
git merge feature_branch_name
```

---
**Remember** to use this sensible workflow for using a development branch from two machines (laptop, desktop) and deploying the app from a remote server.

# Setup Remote Repository for syncing
If you've created a repository in GitHub already, say "opine_dashboard" & set the permission as Public or Private:

```
git remote add origin https://github.com/dagny099/opine_dashboard.git
git branch -M main
git push -u origin main
```

---

