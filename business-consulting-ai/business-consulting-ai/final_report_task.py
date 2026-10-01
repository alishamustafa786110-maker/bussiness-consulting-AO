from crewai import Task


def create_final_report_task(agent, context_tasks) -> Task:
    return Task(
        description="""
Act as the senior consulting partner.

Synthesize all prior consulting work into the final report for this business:

BUSINESS IDEA:
{business_idea}

TARGET MARKET:
{target_market}

BUDGET:
{budget}

Create a professional report with exactly these sections:

# Business Strategy Report

## 1. Executive Summary
## 2. Business Concept
## 3. Market Analysis
## 4. Customer Analysis
## 5. Competitive Landscape
## 6. Business Model
## 7. Positioning and Differentiation
## 8. Go-To-Market Strategy
## 9. Marketing and Sales Strategy
## 10. Financial Framework
## 11. Risk Analysis
## 12. 90-Day Action Plan
## 13. Key Assumptions
## 14. Validation Checklist
## 15. Strategic Synthesis

Rules:
- Be practical and specific.
- Do not fabricate statistics, current prices, market shares, or company facts.
- Clearly label assumptions and hypotheses.
- If the team lacks current external data, say what should be researched.
- Resolve contradictions between earlier analyses.
- Avoid repeating the same point in multiple sections.
- The report should help a founder decide what to test next.
""",
        expected_output="""
A polished, self-contained business strategy report in Markdown using
the exact requested section structure.
""",
        agent=agent,
        context=context_tasks,
    )
