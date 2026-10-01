from crewai import Task


def create_financial_task(agent, context_tasks) -> Task:
    return Task(
        description="""
Create a financial and risk framework for the business idea using the research
and strategy context provided.

BUSINESS IDEA:
{business_idea}

BUDGET:
{budget}

Include:
1. Revenue model
2. Pricing assumptions
3. Major cost categories
4. Simple unit-economics framework
5. Example scenario assumptions
6. Cash-flow risks
7. Operational risks
8. Regulatory/compliance considerations that should be checked
9. Key metrics to monitor
10. What financial data the founder must validate

Use illustrative assumptions only when exact numbers are not available.
Clearly label every example as an assumption or scenario.
""",
        expected_output="""
A transparent financial and risk memo. Include formulas or simple example
scenarios where useful, but clearly label assumptions.
""",
        agent=agent,
        context=context_tasks,
    )
