import os
import litellm
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

litellm.use_litellm_proxy = True


def get_company_info(ticker: str) -> dict:
    """
    Retrieves basic information for a given stock ticker.
    This is a mock tool for demonstration purposes.
    """
    print(f"\n--- TOOL CALLED: get_company_info for ticker: {ticker} ---\n")
    mock_db = {
        "GOOGL": {"name": "Alphabet Inc.", "sector": "Communication Services"},
        "MSFT": {"name": "Microsoft Corporation", "sector": "Technology"},
        "ADBE": {"name": "Adobe Inc.", "sector": "Technology"}
    }
    return mock_db.get(
        ticker.upper(),
        {"error": f"Information for ticker '{ticker}' not found."}
    )


AGENT_INSTRUCTION = """
You are a financial analyst assistant.
Your primary goal is to provide concise, factual information about public
companies based on their stock ticker.  You have access to a powerful
tool: `get_company_info`.
When a user asks for information about a company and provides a stock ticker
(e.g., "Tell me about MSFT"), you MUST use the `get_company_info` tool to
retrieve the data.  After the tool returns the information, present it to
the user in a clear and readable format.
Do not make up information. If the tool returns an error or indicates
that a ticker was not found, you must inform the user about this fact
directly.
"""

root_agent = Agent(
    model=LiteLlm(model="gemini-2.5-pro-(US)", temperature=0.8),
    name="financial_analyst_agent",
    instruction=AGENT_INSTRUCTION,
    tools=[get_company_info],
)
