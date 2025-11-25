---
layout: single
title: "Let's Connect"
description: "Get in touch with Barbara Hidalgo-Sotelo for data science, cognitive systems, and AI strategy work."
permalink: /contact/
classes: wide contact-page
author_profile: false
header:
  overlay_color: "#1e3a5f"
  overlay_filter: 0.7
excerpt: >
  I'm always interested in conversations about data products, cognitive approaches to AI,
  and collaborative projects that make complex information accessible.
---

<div class="page-shell section-stack contact-page">

<div class="contact-intro">
  <p>
    Open to <strong>Data Scientist</strong>, <strong>AI Consultant</strong>, and <strong>AI Strategist</strong> roles,
    plus collaborative projects at the intersection of data products, knowledge graphs, and pragmatic MLOps.
  </p>
  <p>
    Hiring? Download my latest <a href="/assets/docs/Barbara_Hidalgo-Sotelo_CURRENT_RESUME_2025.pdf" target="_blank" rel="noopener">resume (PDF)</a>
    or explore my detailed <a href="/about/">journey</a> to see how I build data products end to end.
  </p>
</div>

## Reach Out

<div class="contact-cards">
  <a href="/assets/docs/Barbara_Hidalgo-Sotelo_CURRENT_RESUME_2025.pdf" target="_blank" rel="noopener" class="contact-card contact-card--resume">
    <div class="contact-card__icon">
      <i class="fas fa-file-alt" aria-hidden="true"></i>
    </div>
    <div class="contact-card__body">
      <h3>Resume (PDF)</h3>
      <span>Latest experience & case studies</span>
    </div>
  </a>

  <a href="mailto:barbs@barbhs.com" class="contact-card contact-card--email">
    <div class="contact-card__icon">
      <i class="fas fa-envelope" aria-hidden="true"></i>
    </div>
    <div class="contact-card__body">
      <h3>Email</h3>
      <span>barbs@balex.com</span>
    </div>
  </a>

  <a href="https://www.linkedin.com/in/barbara-hidalgo-sotelo/" target="_blank" rel="noopener" class="contact-card contact-card--linkedin">
    <div class="contact-card__icon">
      <i class="fab fa-linkedin" aria-hidden="true"></i>
    </div>
    <div class="contact-card__body">
      <h3>LinkedIn</h3>
      <span>/in/barbara-hidalgo-sotelo</span>
    </div>
  </a>

  <!-- <a href="https://github.com/dagny099" target="_blank" rel="noopener" class="contact-card contact-card--github">
    <div class="contact-card__icon">
      <i class="fab fa-github" aria-hidden="true"></i>
    </div>
    <div class="contact-card__body">
      <h3>GitHub</h3>
      <span>dagny099</span>
    </div>
  </a>
</div> -->

---

## Send a Message

<div class="contact-form-wrapper">
  <p class="form-intro">Have a question or want to discuss a project? Drop me a note below.</p>

  <form action="https://formspree.io/f/mgvlqkve" method="POST" class="contact-form">
    <div class="form-grid">
      <div class="form-group">
        <label for="name">Your name</label>
        <input type="text" id="name" name="name" placeholder="Jane Smith" required />
      </div>
      <div class="form-group">
        <label for="email">Your email</label>
        <input type="email" id="email" name="_replyto" placeholder="jane@example.com" required />
      </div>
    </div>
    <div class="form-group">
      <label for="message">Message</label>
      <textarea id="message" name="message" rows="5" placeholder="What's on your mind?" required></textarea>
    </div>
    <input type="hidden" name="_subject" value="Portfolio Contact" />
    <input type="text" name="_gotcha" style="display:none" />
    <button type="submit" class="btn btn--primary btn--large">
      <i class="fas fa-paper-plane" aria-hidden="true"></i> Send Message
    </button>
  </form>
</div>

</div>

<style>
/* =============================================
   Contact Page Styles
   ============================================= */

/* Intro section */
.contact-intro {
  max-width: 720px;
  margin: 0 auto 2rem;
  text-align: center;
  font-size: 1.1rem;
  line-height: 1.6;
  color: #495057;
}

/* Contact method cards */
.contact-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin: 1.5rem 0 2.5rem;
}

.contact-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 1.5rem;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  text-decoration: none;
  transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
}

.contact-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  text-decoration: none;
}

.contact-card__icon {
  flex: 0 0 auto;
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  font-size: 1.4rem;
}

.contact-card__body h3 {
  margin: 0 0 0.2rem;
  font-size: 1rem;
  font-weight: 700;
  color: #1a1a2e;
}

.contact-card__body span {
  font-size: 0.9rem;
  color: #6c757d;
}

/* Card accent colors */
.contact-card--email .contact-card__icon {
  background: #e7f5f4;
  color: #0e7490;
}
.contact-card--email:hover {
  border-color: rgba(14, 116, 144, 0.3);
}

.contact-card--resume .contact-card__icon {
  background: #f4f0ff;
  color: #6b21a8;
}
.contact-card--resume:hover {
  border-color: rgba(107, 33, 168, 0.3);
}

.contact-card--linkedin .contact-card__icon {
  background: #e8f4fc;
  color: #0077b5;
}
.contact-card--linkedin:hover {
  border-color: rgba(0, 119, 181, 0.3);
}

.contact-card--github .contact-card__icon {
  background: #f3f4f6;
  color: #24292e;
}
.contact-card--github:hover {
  border-color: rgba(36, 41, 46, 0.3);
}

/* Form wrapper card */
.contact-form-wrapper {
  max-width: 640px;
  margin: 1.5rem auto 0;
  padding: 2rem;
  background: #f8f9fa;
  border: 1px solid rgba(0,0,0,0.06);
  border-radius: 16px;
}

.form-intro {
  text-align: center;
  color: #6c757d;
  margin: 0 0 1.5rem;
}

/* Form grid for name/email */
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 540px) {
  .form-grid {
    grid-template-columns: 1fr;
  }
}

.form-group {
  margin-bottom: 1rem;
}

.contact-form label {
  display: block;
  margin-bottom: 0.4rem;
  font-weight: 600;
  font-size: 0.95rem;
  color: #374151;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #fff;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.contact-form input:focus,
.contact-form textarea:focus {
  outline: none;
  border-color: #0e7490;
  box-shadow: 0 0 0 3px rgba(14, 116, 144, 0.15);
}

.contact-form input::placeholder,
.contact-form textarea::placeholder {
  color: #9ca3af;
}

.contact-form textarea {
  resize: vertical;
  min-height: 120px;
}

/* Submit button */
.contact-form .btn--primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  padding: 0.85rem 1.75rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 10px;
  background: #0e7490;
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background 0.15s ease, transform 0.15s ease;
}

.contact-form .btn--primary:hover {
  background: #0c6478;
  transform: translateY(-1px);
}

/* Divider styling */
.contact-page hr {
  border: 0;
  border-top: 1px solid #e5e7eb;
  margin: 2.5rem 0;
}

/* Section headers */
.contact-page h2 {
  text-align: center;
  color: #1a1a2e;
  margin-bottom: 0.5rem;
}
</style>
