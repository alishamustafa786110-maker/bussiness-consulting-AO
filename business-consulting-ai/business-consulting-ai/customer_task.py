from crewai import Task


def create_customer_task(agent) -> Task:
    return Task(
        description="""
Analyze the customers for this business idea:

BUSINESS IDEA:
{business_idea}

TARGET MARKET:
{target_market}

Identify:
1. Ideal customer profile
2. 2-4 useful customer segments
3. Customer pain points
4. Jobs-to-be-done / needs
5. Buying triggers
6. Common objections
7. Value drivers
8. Customer research questions that should be validated

Do not claim that a customer behavior is a verified fact unless it is provided in the input.
""",
        expected_output="""
A structured customer analysis including an ideal customer profile,
segments, pain points, buying triggers, objections, and validation questions.
""",
        agent=agent,
    )
