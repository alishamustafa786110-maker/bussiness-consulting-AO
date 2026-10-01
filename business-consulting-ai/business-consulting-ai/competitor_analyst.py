from crewai import Agent

from groq_llm import get_groq_llm


def create_competitor_analyst() -> Agent:
    return Agent(
        role="Competitive Intelligence Consultant",
        goal=(
            "Analyze direct and indirect competitors, likely positioning, pricing logic, "
            "strengths, weaknesses, substitutes, and potential market gaps."
        ),
        backstory=(
            "You are a competitive strategy consultant. When current competitor data "
            "has not been researched with external tools, you label competitor details "
            "as hypotheses instead of presenting them as verified facts."
        ),
        llm=get_groq_llm(),
        allow_delegation=False,
        verbose=False,
    )
