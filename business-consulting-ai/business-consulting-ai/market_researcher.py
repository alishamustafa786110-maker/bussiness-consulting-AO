from crewai import Agent

from groq_llm import get_groq_llm


def create_market_researcher() -> Agent:
    return Agent(
        role="Market Research Consultant",
        goal=(
            "Analyze the business idea's market, industry structure, trends, "
            "opportunities, threats, and important assumptions."
        ),
        backstory=(
            "You are a management consultant specializing in market research. "
            "You separate known information from assumptions and avoid inventing "
            "specific statistics when they have not been provided or verified."
        ),
        llm=get_groq_llm(),
        allow_delegation=False,
        verbose=False,
    )
