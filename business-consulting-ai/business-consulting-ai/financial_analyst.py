from crewai import Agent

from groq_llm import get_groq_llm


def create_financial_analyst() -> Agent:
    return Agent(
        role="Financial and Risk Consultant",
        goal=(
            "Develop a practical financial framework using clearly labeled assumptions, "
            "and identify financial, operational, regulatory, and execution risks."
        ),
        backstory=(
            "You are a business finance and risk consultant. You do not fabricate financial "
            "facts. You create transparent scenarios and identify what the founder must validate."
        ),
        llm=get_groq_llm(),
        allow_delegation=False,
        verbose=False,
    )
