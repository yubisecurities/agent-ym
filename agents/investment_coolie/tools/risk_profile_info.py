import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

url = "https://partner-qa-api.aspero.co.in/forest/opms/risk-profiling"

headers = {
  'Accept': 'application/json',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'x-api-key': os.getenv('B2B2C_DRONA_API'),
}

def get_risk_profile(owner_type: str, owner_id: str) -> dict:
  payload = json.dumps({
    "owner_id": owner_id,
    "owner_type": owner_type
  })
  print(f"Calling Risk Profile {url}", headers, payload)
  response = requests.request("POST", url, headers=headers, data=payload)
  if response.status_code == 200:
    return response.text
  else:
    print("Failed to fetch data. Status code:", response.status_code, response.content)
    return None
