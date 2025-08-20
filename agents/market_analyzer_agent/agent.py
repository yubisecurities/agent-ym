import os
import litellm
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from .tools.company_info import get_company_info
from .tools.listing_info import get_all_listings
from .tools.stock_info import get_stock_index, get_stock

from .utils.prompt import market_analyzer_agent_prompt

load_dotenv()

litellm.use_litellm_proxy = True

root_agent = Agent(
    model=LiteLlm(model="gemini-2.5-pro-(US)", temperature=0.8),
    name="market_analyzer_agent",
    instruction=market_analyzer_agent_prompt,
    tools=[get_company_info, get_all_listings, get_stock_index, get_stock],
)
