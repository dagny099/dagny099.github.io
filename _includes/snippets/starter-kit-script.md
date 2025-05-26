```bash
poetry init
direnv allow .
streamlit run app.py
```

<div class="mermaid">
    graph TD
    S3 --> Lambda
    Lambda -->|Container| ECR
    Lambda --> SNS
    SNS --> Slack
</div>
