# Beginner deployment checklist

## 1. GitHub

Create a repository named:

`business-consulting-ai`

Upload every file in this folder.

Do NOT upload your Groq API key.

## 2. Streamlit Community Cloud

Create a new app and select:

- Repository: your GitHub repository
- Branch: `main`
- Main file: `app.py`
- Python: 3.12

## 3. Add the Groq key

Open the app's Settings / Secrets area and add:

```toml
GROQ_API_KEY = "your-real-groq-api-key"
```

Save, then let Streamlit redeploy.

## 4. Test

Enter:

Business idea:
`AI-powered bookkeeping service for small businesses`

Target market:
`Pakistan`

Budget:
`$10,000`

Then click:

`Generate Business Strategy`

The six agents run sequentially and the Senior Partner produces the final report.
