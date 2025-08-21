import os
import litellm
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import asyncio
import websockets
import json

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

# # Now you can use the runner to interact with your agent
# user_id = "user123"
# session_id = "session456"
# query = input("Enter the query: ")
# content = types.Content(role='user', parts=[types.Part(text=query)])


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

# This is the new part for WebSocket handling
async def handle_websocket_connection(websocket):
    try:
        # Await the initial message from the client
        message = await websocket.recv()
        data = json.loads(message)

        user_id = data.get("user_id", "default_user")
        session_id = data.get("session_id", "default_session")
        query = data.get("query", "") + "client id is " + str(data.get("customerId")) + "and is client type is Client"

        if not query:
            await websocket.send(json.dumps({"error": "Query cannot be empty."}))
            return

        print(f"Received query from client: {query}")

        content = types.Content(role='user', parts=[types.Part(text=query)])

        # Ensure the session exists before running the agent
        await session_service.create_session(user_id=user_id, session_id=session_id, app_name=runner.app_name)

        # Run the agent and stream the responses back to the client
        events = runner.run_async(user_id=user_id, session_id=session_id, new_message=content)
        async for event in events:
            # Check for the final response and send it
            if event.is_final_response():
                response_text = event.content.parts[0].text
                print("Agent Response:", response_text)
                await websocket.send(json.dumps({"response": response_text}))
                break  # Exit after sending the final response

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        await websocket.send(json.dumps({"error": str(e)}))

# Main function to start the WebSocket server
async def main():
    # Change the host and port as needed
    host = "localhost"
    port = 8765
    async with websockets.serve(handle_websocket_connection, host, port):
        print(f"WebSocket server started on ws://{host}:{port}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())