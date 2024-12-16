---
title: "CoverCraft: a Job App Assistant Chatbot"
excerpt: "An LLM assistant to iteratively customize your resume and cover letters"
date: 2024-04-15 # Change this to control the order
classes: [portfolio-page]
category: Project
tags: [NLP, GenAI, App Design, Streamlit]
toc: true
toc_sticky: true  
toc_label: "ToC"  
toc_icon: "sitemap"   
header:
  overlay_color: "#122d50"
  teaser: assets/images/portfolio_thumbnail_desertMJ.jpg
  actions:
    - label: Visit App
      url: https://barbsassistant.streamlit.app
sidebar:
  - title: ""
    image: assets/images/portfolio/jobappassistant_th.jpg
    image_alt: "App Screenshot"
    text: "*README.md: Instructions for my own existence*"
---

## Overview
The app delivers an engaging workflow, enabling users to import existing resumes, edit them interactively, and generate tailored cover letters. It also identifies ATS-relevant keywords to improve application success rates.

### Audience
- **Data scientists** looking to explore how to use LLMs to tailor documents in a directed way.
- **Experienced professionals** refining their application for a career shift.
- **Job seekers** aiming to improve Applicant Tracking System (ATS) compatibility.

## Description
This project is a publicly accessible **Streamlit web application** designed to empower job seekers by streamlining the creation of tailored resumes and cover letters. Using helpful LLMslike OpenAI's GPT-3.5 and GPT-4, the app provides an intuitive and interactive experience for customizing job application materials. By automating key elements of the process—such as keyword optimization and draft generation—the app supports users in presenting their best professional selves.


### Project Highlights

* **Seamless Import Options**:
   - Supports resume input via file upload (PDF, text) or manual text entry
   
* **Interactive Customization**:
   - Sidebar inputs allow users to customize resumes and cover letters with job-specific details
   - Real-time LLM-powered edits for personalized tone and content

* **ATS Keyword Optimization**:
   - Identifies and highlights gaps in keyword relevance based on the job description

* **User-Friendly Outputs**:
   - Enables downloading finalized cover letters and storing session states for later edits

* **Scalable Infrastructure**:
   - Built with Streamlit, ensuring lightweight and adaptable deployment options


## Core Skills

### Tools & Technologies
- **Development Framework**: Streamlit for web app creation
- **NLP & AI**: OpenAI's GPT-3.5/GPT-4 for natural language processing
- **Backend Utilities**: PyPDF2, JSON parsing, and text processing
- **Version Control**: Git
- **Cloud Hosting**: Streamlit Community Cloud

### Technical Skillset
- **Text Parsing**:
   - Extracts applicant details like name, contact information, and professional summary with advanced regular expressions and contextual inference
- **Interactive LLM Integration**:
   - Powers real-time cover letter and resume edits based on user prompts
- **Data Management**:
   - Implements session persistence using Python’s pickle library for seamless state saving
- **Keyword Analysis**:
   - Employs statistical and NLP-based techniques for ATS keyword alignment


## Project Insights

### Implementation Challenges
* **Accurate Information Extraction**:
   - Balancing precision and recall when parsing user-provided resumes to avoid omitting critical details
* **ATS Simulation**:
   - Developing an accessible yet representative ATS keyword scanning system without reliance on proprietary algorithms
* **LLM Responsiveness**:
   - Ensuring the app responds accurately to diverse user prompts, maintaining a balance between automation and interactivity

### Future Development
- **Enhanced Keyword Analysis**: Integrate pre-trained NLP models (e.g., SpaCy, BERT) to refine keyword extraction and relevance scoring
- **Broader File Format Support**: Add functionality for importing/exporting Microsoft Word documents
- **Expanded LLM Features**: Provide detailed user guidance for fine-tuning the tone, structure, and content of resumes and cover letters

---

**Learn More:**   
**[GitHub Repository](https://github.com/dagny099/assistant_author)** | **[Explore App](https://barbsassistant.streamlit.app/)**
