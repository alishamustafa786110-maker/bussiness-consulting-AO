from crewai import Task


def create_market_task(agent) -> Task:
    return Task(
        description="""
Analyze the following business idea from a market and industry perspective:

BUSINESS IDEA:
{business_idea}

TARGET MARKET:
{target_market}

BUDGET:
{budget}

Produce a structured analysis covering:
1. Industry and market overview
2. Relevant market trends
3. Demand drivers
4. Opportunities
5. Threats
6. Important assumptions
7. Questions that require external validation

Do not invent precise market statistics. If a current fact would require web research,
say that it needs verification.
""",
        expected_output="""
A concise but detailed market research memo with clear headings.
Separate likely facts, strategic hypotheses, and items requiring validation.
""",
        agent=agent,
    )
