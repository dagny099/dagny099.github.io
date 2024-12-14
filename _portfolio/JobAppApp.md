---
title: "Job App Assistant Chatbot"
excerpt: "An LLM assistant to customize resume and documents"
date: 2024-04-15 # Change this to control the order
classes: [wide, portfolio-page]
category: Project
tags: [NLP, GenAI, App Design, Streamlit]
header:
  overlay_color: "#122d50"
  teaser: assets/images/unsplash-gallery-image-1-th.jpg
  actions:
    - label: Visit App
      url: https://barbsassistant.streamlit.app
---

## Description
A publicly-available **Streamlit web application** designed to assist users in creating tailored resumes and cover letters for job applications. Powered by advanced language models (LLMs) like OpenAI's GPT-3.5 and GPT-4, the app offers an interactive and user-friendly workflow to refine application materials. 

## Key Features

1. **Resume Import**:
   - Load an existing resume in PDF or text format.
   - Alternatively, type resume content directly into a text box.

2. **Customizable Details**:
   - Input specific job details in the sidebar to customize the outputs.

3. **Applicant Information Extraction**:
   - Automatically extract applicant details from the uploaded resume and display them in the sidebar.
     - Uses text parsing techniques to identify key details like name, contact information, and professional summary.
     - Relies on pattern matching and context-based inference to ensure accuracy, with fallback mechanisms for manual edits.

4. **Cover Letter Drafting**:
   - Generate a first draft of a cover letter based on the resume and job description.
   - Edit the cover letter interactively using the LLM to request changes (e.g., tone, content).

5. **Applicant Tracking System (ATS) Keyword Check**:
   - Perform a basic ATS scan to ensure relevant keywords are present in the resume and cover letter.
     - This scan identifies critical keywords related to job descriptions and compares them with those in the resume and cover letter.
     - While modeled after common ATS systems, it focuses on identifying gaps in keyword alignment rather than emulating a specific proprietary system.

6. **Downloadable Outputs**:
   - Save the finalized cover letter as a text file.

7. **Session Management**:
   - Save and load session states to allow for easy resumption of work.

- **Skills:** 

- **[GitHub Repository](https://github.com/dagny099/assistant_author)** | **[Explore App](https://barbsassistant.streamlit.app/)**
