from crewai import Task


def create_strategy_task(agent, context_tasks) -> Task:
    return Task(
        description="""
Using the market, customer, and competitive analyses provided as context,
develop the core business strategy for:

BUSINESS IDEA:
{business_idea}

TARGET MARKET:
{target_market}

BUDGET:
{budget}

Develop:
1. Value proposition
2. Ideal initial customer
3. Positioning statement
4. Business/revenue model
5. Pricing approach
6. Differentiation strategy
7. Go-to-market strategy
8. Marketing channels
9. Sales approach
10. Key strategic assumptions
11. First experiments to validate the strategy

Do not invent current market facts. Make assumptions explicit.
""",
        expected_output="""
A coherent business strategy memo with practical choices,
assumptions, trade-offs, and validation experiments.
""",
        agent=agent,
        context=context_tasks,
    )
