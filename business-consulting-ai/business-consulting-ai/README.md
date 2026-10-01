# AI Business Consulting Firm

A beginner-friendly multi-agent business consulting application built with:

- CrewAI 1.15.23
- Groq
- `openai/gpt-oss-20b`
- Streamlit 1.64.0

## Agents

1. Market Researcher
2. Customer Researcher
3. Competitor Analyst
4. Business Strategist
5. Financial & Risk Analyst
6. Senior Consulting Partner

## Repository structure

```text
business-consulting-ai/
├── app.py
├── groq_llm.py
├── consulting_crew.py
├── market_researcher.py
├── customer_researcher.py
├── competitor_analyst.py
├── business_strategist.py
├── financial_analyst.py
├── senior_partner.py
├── market_task.py
├── customer_task.py
├── competitor_task.py
├── strategy_task.py
├── financial_task.py
├── final_report_task.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Deployment

This project is designed for GitHub + Streamlit Community Cloud.

1. Push this repository to GitHub.
2. Create a Streamlit Community Cloud app using `app.py`.
3. Choose Python 3.12 in Advanced settings if prompted.
4. In the app's Secrets settings, add:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

5. Deploy.

Never commit the API key to GitHub.

## Important limitation

This first version is an LLM-based consulting workflow. The market and competitor
agents do not automatically browse the web. Their outputs therefore distinguish
hypotheses and validation requirements from verified current data.

Groq's GPT-OSS models support browser search, so a later version can add current
web research while keeping this six-agent architecture.
