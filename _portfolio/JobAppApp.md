---
title: "CareerCraft: Job Application Assistant"
excerpt: "An intelligent assistant for creating customized resumes and cover letters using advanced NLP."
date: 2024-04-15
classes: [portfolio-page]
category: Project
tags: [NLP, GenAI, App Design, Streamlit, Heroku]
toc: true
toc_sticky: true  
toc_label: "Contents"  
toc_icon: "sitemap"
header:
  overlay_color: "#122d50"
  teaser: assets/images/portfolio_thumbnail_desertMJ.jpg
  actions:
    - label: Visit App on Heroku
      url: https://careercraft.barbhs.com
    - label: GitHub Repository
      url: https://github.com/dagny099/assistant_author
sidebar:
  - title: "CareerCraft App"
    image: assets/images/portfolio/jobappassistant_th.jpg
    image_alt: "CareerCraft App Screenshot"
    text: "*Elevate your career opportunities with AI.*"
---

## 🚀 Project Overview
CareerCraft empowers job seekers to effortlessly create highly customized resumes and cover letters using sophisticated natural language processing (NLP) techniques powered by OpenAI's GPT models. Initially deployed on Streamlit Cloud, the application now primarily resides on Heroku, ensuring enhanced stability, improved responsiveness, and persistent availability.

### 🎯 Who Should Use CareerCraft?
- **Data Scientists** exploring practical NLP and GenAI integration
- **Professionals** aiming for career transitions or advancements
- **Job Applicants** seeking ATS optimization and personalized materials


## 🛠️ Key Features

<div style="float: right; margin: 10px; width: 40%;">
  <img src="assets/images/portfolio/DataFlow-Diagram-CareerCraft_v1.png"" 
       alt="CoverCraft App Screenshot" style="width:100%; height:auto;">
  <em style="display:block; text-align:center; font-size:0.9em;">CareerCraft Workflow</em>
</div>

### 📁 Multiple Import Formats
- Easily upload resumes via PDF, text files, or manual entry

### 🎨 Interactive Customization
- User-friendly sidebar to edit resumes and cover letters dynamically
- AI-driven content generation and editing based on user specifications

### 🔍 ATS Optimization
- Automated keyword matching to maximize ATS compatibility and success

### 💾 Convenient Outputs
- Immediate download options for cover letters and session management for ongoing edits

### ☁️ Robust Hosting Infrastructure
- Primary deployment on **Heroku**, with fallback on **Streamlit Cloud** for redundancy

## Core Skills

<div style="float: right; margin: 10px; width: 40%;">
  <img src="assets/images/portfolio/CareerCraft_techstack_v1.png"
       alt="CoverCraft App Screenshot" style="width:100%; height:auto;">
  <em style="display:block; text-align:center; font-size:0.9em;">CareerCraft Tech Stack</em>
</div>


### 🖥️ Tools & Technologies
- **Frontend**: Streamlit Web Framework
- **AI/NLP**: GPT-3.5 & GPT-4 from OpenAI
- **Backend Utilities**: PyPDF2, JSON, pickle for session state management
- **Deployment**: Heroku (Primary), Streamlit Cloud (Backup)
- **Version Control**: GitHub

### 📈 Technical Skillset
- **Text Parsing & Extraction**: Accurately extracts key applicant information (name, skills, contact details).
- **Interactive LLM Integration**: Provides real-time feedback and editing suggestions powered by GPT models.
- **Persistent Session Management**: Seamless continuation of previous sessions through serialization.


## Project Insights

### 🌟 Challenges & Solutions
- **Information Accuracy**: Implemented NLP best practices to balance accuracy with flexibility.
- **ATS Keyword Simulation**: Developed a realistic keyword-matching approach without proprietary algorithms.
- **Responsive AI Interaction**: Optimized LLM interactions for prompt responsiveness and user satisfaction.

## 🚧 Future Directions
- **Advanced Keyword Analysis**: Integrate NLP libraries (SpaCy, BERT) to refine ATS matching.
- **Broader Document Support**: Add MS Word document compatibility.
- **Enhanced AI Features**: Offer detailed guidance for nuanced editing of professional documents.

---

**Explore Further:**  
[🔗 Visit CareerCraft on Heroku](https://careercraft.barbhs.com) | [📘 GitHub Repository](https://github.com/dagny099/assistant_author)
