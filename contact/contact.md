---
layout: single
title: "Contact"
permalink: /contact/
classes: wide
author_profile: false     # keep the page clean and centered
---

## Let’s talk

I’m open to mid–senior **Data Scientist**, **AI Consultant**, and **AI Strategist** roles, plus collaborative projects at the intersection of data products, knowledge graphs, and pragmatic MLOps.

- **Email:** <a class="btn btn--primary" href="mailto:barb@barbhs.com">barb@barbhs.com</a>
- **GitHub:** <a class="btn" href="https://github.com/dagny099">dagny099</a>
- **LinkedIn:** <a class="btn" href="https://www.linkedin.com/in/barbarahidalgo">/in/barbarahidalgo</a>

---

### Quick message form (optional)
<!-- 
> If you use **Formspree** (recommended for GitHub Pages), replace the `action` URL below with your Formspree endpoint and it will just work.  
> If you host on **Netlify**, change the `<form>` tag to `netlify` and remove the `action` attribute (see commented block).
-->
<form action="https://formspree.io/f/mgvlqkve" method="POST" class="contact-form">
  <div class="grid__wrapper">
    <div class="grid__item">
      <label for="name">Your name</label>
      <input type="text" id="name" name="name" required />
    </div>
    <div class="grid__item">
      <label for="email">Your email</label>
      <input type="email" id="email" name="_replyto" required />
    </div>
  </div>
  <label for="message">Message</label>
  <textarea id="message" name="message" rows="6" required></textarea>
  <!-- Optional hidden fields -->
  <input type="hidden" name="_subject" value="Portfolio Contact" />
  <input type="text" name="_gotcha" style="display:none" />
  <button type="submit" class="btn btn--primary">Send</button>
</form>

<!-- Netlify version (uncomment if hosting on Netlify)
<form name="contact" method="POST" data-netlify="true" class="contact-form">
  <input type="hidden" name="form-name" value="contact">
  <div class="grid__wrapper">
    <div class="grid__item">
      <label for="name">Your name</label>
      <input type="text" id="name" name="name" required />
    </div>
    <div class="grid__item">
      <label for="email">Your email</label>
      <input type="email" id="email" name="email" required />
    </div>
  </div>
  <label for="message">Message</label>
  <textarea id="message" name="message" rows="6" required></textarea>
  <button type="submit" class="btn btn--primary">Send</button>
</form>
-->

<style>
.contact-form label { display:block; margin-top: .75rem; font-weight:600; }
.contact-form input, .contact-form textarea { width:100%; }
.grid__wrapper { display:grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
@media (max-width: 768px) { .grid__wrapper { grid-template-columns: 1fr; } }
</style>