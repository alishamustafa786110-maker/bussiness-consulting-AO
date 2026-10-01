from crewai import Crew, Process

from market_researcher import create_market_researcher
from customer_researcher import create_customer_researcher
from competitor_analyst import create_competitor_analyst
from business_strategist import create_business_strategist
from financial_analyst import create_financial_analyst
from senior_partner import create_senior_partner

from market_task import create_market_task
from customer_task import create_customer_task
from competitor_task import create_competitor_task
from strategy_task import create_strategy_task
from financial_task import create_financial_task
from final_report_task import create_final_report_task


def run_consulting_crew(
    business_idea: str,
    target_market: str,
    budget: str,
) -> str:
    """Run the six-agent consulting workflow and return the final report."""

    market_agent = create_market_researcher()
    customer_agent = create_customer_researcher()
    competitor_agent = create_competitor_analyst()
    strategy_agent = create_business_strategist()
    financial_agent = create_financial_analyst()
    senior_partner = create_senior_partner()

    market_task = create_market_task(market_agent)
    customer_task = create_customer_task(customer_agent)
    competitor_task = create_competitor_task(competitor_agent)

    strategy_task = create_strategy_task(
        strategy_agent,
        [market_task, customer_task, competitor_task],
    )

    financial_task = create_financial_task(
        financial_agent,
        [market_task, customer_task, competitor_task, strategy_task],
    )

    final_report_task = create_final_report_task(
        senior_partner,
        [
            market_task,
            customer_task,
            competitor_task,
            strategy_task,
            financial_task,
        ],
    )

    crew = Crew(
        agents=[
            market_agent,
            customer_agent,
            competitor_agent,
            strategy_agent,
            financial_agent,
            senior_partner,
        ],
        tasks=[
            market_task,
            customer_task,
            competitor_task,
            strategy_task,
            financial_task,
            final_report_task,
        ],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff(
        inputs={
            "business_idea": business_idea,
            "target_market": target_market,
            "budget": budget,
        }
    )

    return result.raw
