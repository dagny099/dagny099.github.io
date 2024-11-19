---
title: "Workout Dashboard"
excerpt: "Build an interactive dashboard of my workouts backed by AWS Relational Database (RDS)"
order: 2 # Lower numbers appear first
date: 2024-02-15 # Change this to control the order
classes: [wide, portfolio-page]
category: Project
tags: [Data Science, Data Visualization, SQL, Streamlit, AWS, RDS]
header:
  image: assets/images/
  teaser: assets/images/powerlines_pic_th.jpg
---

- **Description:** A full-stack data analytics platform that pulls workout data from my MapMyRun profile into an actionable workout dashboard application. This web application combines data ingestion and cleaning, data modeling and access, and machine learning to help me visualize and understand my training patterns as viewed on my configurable dashboard. 

- **Key Features:**
  - **Data Ingestion Pipeline**: Engineered an ETL pipeline to periodically export workout data from MapMyRun's CSV exports and ingest the new entries (after cleaning and enriching the data) into a structured MySQL database (local and remote versions)
  - **Interactive Analytics Dashboard**: Built a responsive web interface using Streamlit and Plotly tha visualizes key workout metrics and training trends interactively
  - **Practice SQL Queries**: Integrated a way to execute SQL queries via the interactive dashboard to practice SQL query skills using data that I'm personally familiar with and invested in understanding more deeply
  - **Performance Optimization**: Implemented efficient data storage and retrieval mechanisms to handle large workout history datasets while maintaining responsive dashboard performance

- **Skills:**
  - **Languages & Frameworks**: Python, Bash scripting, MySQL, AWS EC2 and RDS configuration and management
  - **Data Visualization**: Plotly, Streamlit, Workout metric design and layout
  - **Database**: MySQL, AWS RDS, Data modeling, Query generation
  - **Machine Learning**: Anomaly detection for data cleaning, unsupervised learning and clustering algorithms for workout classification
  - **Development Tools**: Poetry for dependency management, Git

- **[GitHub Repository](https://github.com/dagny099/build_workout_dashboard/)** | **[Read More](https://workouts.barbhs.com/)**
