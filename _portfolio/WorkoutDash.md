---
title: "A Personal Workout Analytics Dashboard"
excerpt: "An interactive dashboard of my workouts backed by AWS Relational Database (RDS)"
date: 2024-02-15 # Change this to control the order
classes: [portfolio-page]
category: Project
tags: [Data Science, Data Visualization, SQL, Streamlit, AWS, RDS]
toc: true
toc_sticky: true  
toc_label: "ToC"  
toc_icon: "sitemap"   # also nice: compass, clipboard-list
header:
  image: assets/images/
  overlay_color: "#6b7fa1"
  teaser: assets/images/portfolio/barbDash_Viz_teaser.jpg
sidebar:
  - title: ""
    image: assets/images/portfolio/barbDash_Viz_side.jpg
    text: "*Where SQL meets sweat equity, insights emerge*"
---

## Overview
A data-driven personal project that transforms raw workout data from MapMyRun into actionable insights through a custom MySQL database and analytics dashboard. This project combines personal fitness tracking with practical data engineering and SQL skill development, creating a meaningful way to learn through real-world data.

### Audience
- Geeky fitness enthusiasts interested in deeper workout analytics
- Data profesionals with desires to practice data engineering with personal data
- Anyone interested in gaining greater control of and insights from their data
 
## Description

This project is a custom-built, end-to-end data analytics application designed to provide **motivation to improve my exercise habits**, opportunities to **practice data engineering skills**, and greater **control over my personal data**, encouraging me to uncover meaningful insights. Leveraging data from my MapMyRun profile, my app uses an ETL pipeline to clean, enrich, and analyze fitness metrics. The processed data is stored in a MySQL database hosted on AWS RDS, enabling real-time access to clean, structured workout records. A dashboard offers actionable visualizations that help me track trends, identify progress, and stay motivated toward my fitness goals.

By bringing MapMyRun data under my personal control, this solution ensures long-term data ownership and accessibility, independent of third-party platform changes. The project is a blend of technical skill-building and personal motivation, driven by a desire to uncover actionable insights from data I intuitively understand. This project aims to create a central fitness analytics hub, refine my technical skills in SQL, cloud services, and application development while promoting long-term data ownership and fitness empowerment.

### Project Highlights

- **Data Pipeline Architecture**
   - Extracts workout data using a custom automation script
   - Implements data cleaning and preprocessing
   - Ensures data quality through validation steps
   - Prevents duplicate entries through workout ID tracking

- **Database Design**
   - Utilizes MySQL for structured data storage
   - Implements proper schema design for workout metrics
   - Supports both local development and cloud deployment

- **Environment Management**
   - Secure credential handling through environment variables
   - Configuration management using TOML
   - Local Development/Production environment switching
   - Proper connection handling and resource cleanup

## Core Skills

### Tools & Technologies

- **Languages**: Python
- **Database**: MySQL
- **Cloud Services**: AWS RDS
- **Configuration**: TOML
- **Data Source**: MapMyRun (for now)

### Technical Skillset
- Data Engineering
  - ETL pipeline development
  - Data cleaning and preprocessing
  - Database schema design
  - Error handling and logging
  
- Software Development
  - Python programming
  - Configuration management
  - Environment handling
  - Version control
  
- Cloud & Infrastructure
  - AWS RDS database deployment
  - Secure credential management
  - Production environment setup


## Project Insights

### Implementation Challenges
- Preventing duplicate workout entries through robust ID tracking and verification systems
- Managing secure database connections across development and production environments
- Ensuring data quality through comprehensive cleaning, enrichment, and validation pipelines


### Future Development
* **Analytics Expansion**
   - Add advanced workout metrics
   - Implement trend analysis
   - Create performance forecasting

* **Technical Improvements**
   - Add automated testing
   - Implement CI/CD pipeline
   - Add comprehensive logging

* **User Experience**
   <!-- - Develop web interface -->
   - Fix authenticaion method for visualization dashboard
   - Create automated reporting
   - Implement notification system

<!-- This project demonstrates the practical application of data engineering principles to personal fitness data, creating a valuable tool for workout analysis while serving as a platform for technical skill development. It showcases the implementation of proper software development practices, from configuration management to production deployment considerations. -->
---

**Learn More:**   
**[GitHub Repository](https://github.com/dagny099/build_workout_dashboard/)** | **[Explore App](https://workouts.barbhs.com/)**
