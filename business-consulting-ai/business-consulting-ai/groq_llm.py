import os

from crewai import LLM


MODEL_NAME = "openai/gpt-oss-20b"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"


def get_groq_llm() -> LLM:
    """Create the shared Groq LLM configuration for all agents."""
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. Add it to Streamlit Secrets "
            "or set it as an environment variable."
        )

    return LLM(
        model=MODEL_NAME,
        custom_openai=True,
        base_url=GROQ_BASE_URL,
        api_key=api_key,
        temperature=0.2,
        max_completion_tokens=5000,
    )
