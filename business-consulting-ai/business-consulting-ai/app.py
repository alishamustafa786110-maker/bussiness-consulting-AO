import os

import streamlit as st

from consulting_crew import run_consulting_crew


st.set_page_config(
    page_title="AI Business Consulting Firm",
    page_icon="📊",
    layout="wide",
)


def configure_secrets() -> None:
    """Make Streamlit Cloud secrets available to the application."""
    if os.getenv("GROQ_API_KEY"):
        return

    try:
        secret = st.secrets.get("GROQ_API_KEY")
    except Exception:
        secret = None

    if secret:
        os.environ["GROQ_API_KEY"] = str(secret)


configure_secrets()


st.title("📊 AI Business Consulting Firm")
st.caption(
    "A six-agent CrewAI team that turns a business idea into a structured strategy report."
)

with st.sidebar:
    st.header("Business Inputs")

    target_market = st.text_input(
        "Target market",
        placeholder="e.g. Pakistan, UAE, global",
    )

    budget = st.text_input(
        "Available budget",
        placeholder="e.g. $10,000",
    )

    st.divider()
    st.markdown(
        "**Consulting team**\n"
        "- Market Researcher\n"
        "- Customer Researcher\n"
        "- Competitor Analyst\n"
        "- Business Strategist\n"
        "- Financial & Risk Analyst\n"
        "- Senior Consulting Partner"
    )

business_idea = st.text_area(
    "Describe your business idea",
    height=180,
    placeholder=(
        "Example: I want to build an AI-powered bookkeeping service "
        "for small businesses in Pakistan."
    ),
)

generate = st.button(
    "🚀 Generate Business Strategy",
    type="primary",
    use_container_width=True,
)

if generate:
    if not os.getenv("GROQ_API_KEY"):
        st.error(
            "GROQ_API_KEY is missing. Add it to Streamlit Secrets before running the app."
        )
        st.stop()

    if not business_idea.strip():
        st.warning("Please describe your business idea.")
        st.stop()

    if not target_market.strip():
        st.warning("Please enter a target market.")
        st.stop()

    with st.status("Consulting team is working...", expanded=True) as status:
        st.write("🔎 Market Researcher analyzing the industry...")
        st.write("👥 Customer Researcher analyzing customer segments...")
        st.write("🏁 Competitor Analyst analyzing the competitive landscape...")
        st.write("🧭 Business Strategist developing the strategy...")
        st.write("💰 Financial Analyst building the financial and risk framework...")
        st.write("🧠 Senior Partner synthesizing the final report...")

        try:
            report = run_consulting_crew(
                business_idea=business_idea.strip(),
                target_market=target_market.strip(),
                budget=budget.strip() or "Not specified",
            )
            status.update(
                label="Consulting report completed",
                state="complete",
                expanded=False,
            )
        except Exception as exc:
            status.update(
                label="The consulting run failed",
                state="error",
                expanded=True,
            )
            st.exception(exc)
            st.stop()

    st.success("Your business strategy report is ready.")

    st.markdown(report)

    st.download_button(
        label="⬇️ Download Report",
        data=report,
        file_name="business_strategy_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
