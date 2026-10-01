from crewai import Agent

from groq_llm import get_groq_llm


def create_senior_partner() -> Agent:
    return Agent(
        role="Senior Consulting Partner",
        goal=(
            "Synthesize the consulting team's work into a clear, internally consistent, "
            "actionable business strategy report."
        ),
        backstory=(
            "You are the senior partner reviewing work from a multidisciplinary consulting team. "
            "You challenge weak assumptions, resolve contradictions, remove duplication, and make "
            "the final report useful to a business founder."
        ),
        llm=get_groq_llm(),
        allow_delegation=False,
        verbose=False,
    )
