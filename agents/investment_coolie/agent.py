import os
import litellm
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import asyncio

# Updated Imports
from agents.investment_coolie.tools.company_info import get_company_info
from agents.investment_coolie.tools.listing_info import get_inventory
from agents.investment_coolie.tools.stock_info import get_stock_index, get_stock
from agents.investment_coolie.tools.risk_profile_info import get_risk_profile
from agents.investment_coolie.tools.trades_info import get_trades_data
from agents.investment_coolie.tools.client_info import get_client_details
from agents.investment_coolie.tools.notification import notify

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


from agents.investment_coolie.utils.prompt import investment_coolie_prompt 

load_dotenv()

litellm.use_litellm_proxy = True

root_agent = Agent(
    model=LiteLlm(model="gemini-2.5-pro-(US)", temperature=0.8),
    name="investment_coolie",
    instruction=investment_coolie_prompt,
    tools=[get_company_info, get_inventory, get_stock_index, get_stock, get_risk_profile, get_trades_data, notify, get_client_details],
)


# Set up a session service (using in-memory for this example)
session_service = InMemorySessionService()

# Create a Runner instance
runner = Runner(
    agent=root_agent,
    app_name="investment_coolie",
    session_service=session_service
)

# Now you can use the runner to interact with your agent
user_id = "user123"
session_id = "session456"
query = input("Enter the query: ")
content = types.Content(role='user', parts=[types.Part(text=query)])


# Run the agent asynchronously using the runner
async def interact_with_agent():
    await session_service.create_session(
        user_id=user_id,
        session_id=session_id,
        app_name=runner.app_name  # It's good practice to pass app_name
    )

    events = runner.run_async(user_id=user_id, session_id=session_id, new_message=content)
    async for event in events:
        if event.is_final_response():
            print("Agent Response:", event.content.parts[0].text)

if __name__ == "__main__":
    asyncio.run(interact_with_agent())