from crewai import Agent

from groq_llm import get_groq_llm


def create_business_strategist() -> Agent:
    return Agent(
        role="Business Strategy Consultant",
        goal=(
            "Turn market, customer, and competitive findings into a coherent business "
            "model, value proposition, positioning, pricing approach, and go-to-market strategy."
        ),
        backstory=(
            "You are a senior strategy consultant who synthesizes research into practical "
            "strategic choices. You explicitly state assumptions and trade-offs."
        ),
        llm=get_groq_llm(),
        allow_delegation=False,
        verbose=False,
    )
