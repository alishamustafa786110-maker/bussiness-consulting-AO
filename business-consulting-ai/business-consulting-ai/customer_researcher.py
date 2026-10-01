from crewai import Agent

from groq_llm import get_groq_llm


def create_customer_researcher() -> Agent:
    return Agent(
        role="Customer Research Consultant",
        goal=(
            "Identify the most relevant customer segments, ideal customer profile, "
            "customer needs, pain points, buying behavior, objections, and value drivers."
        ),
        backstory=(
            "You are a customer strategy consultant. You think in terms of customer "
            "segments and jobs-to-be-done, and clearly distinguish hypotheses from facts."
        ),
        llm=get_groq_llm(),
        allow_delegation=False,
        verbose=False,
    )
