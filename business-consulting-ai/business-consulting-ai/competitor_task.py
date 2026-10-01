from crewai import Task


def create_competitor_task(agent) -> Task:
    return Task(
        description="""
Analyze the competitive landscape for:

BUSINESS IDEA:
{business_idea}

TARGET MARKET:
{target_market}

Identify:
1. Likely direct competitors
2. Indirect competitors and substitutes
3. Common competitor positioning
4. Typical pricing models
5. Potential competitor strengths and weaknesses
6. Possible differentiation opportunities
7. Data that must be verified with current external research

Because this version does not automatically browse the web, do not present
specific current competitor prices, market shares, or company facts as verified.
Clearly label hypotheses.
""",
        expected_output="""
A competitive landscape memo that distinguishes hypotheses from facts
and identifies practical differentiation opportunities.
""",
        agent=agent,
    )
