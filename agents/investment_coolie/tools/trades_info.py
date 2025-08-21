import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://partner-qa-api.aspero.co.in/tms/api/v2/trades/trades_for_owner"

payload = {}
headers = {
  'accept': 'application/json',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Authorization': os.getenv('B2B2C_API_KEY'),
  'Current-Entity-Id': os.getenv('B2B2C_API_ENTITY'),
  'channel': os.getenv('B2B2C_API_CHANNEL'),
  'content-type': 'application/json',
  'current-group': 'distributor',
  'if-none-match': 'W/"2eba60fc3744ad23b378c6fd47d5a2e2"',
  'origin': 'https://partner-qa.aspero.co.in',
  'priority': 'u=1, i',
  'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
  'x-request-id': '01e26e7e-0112-4736-9d94-19d45f3c7bcc'
}

def get_trades_data(owner_id: str, owner_type: str):
    query = f"owner_id={owner_id}&owner_type={owner_type}"
    updated_url = url + "?" + query
    response = requests.request("GET", updated_url, headers=headers, data=payload)
    print(f"Calling Risk Profile {updated_url}", headers, payload)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch data. Status code:", response.status_code, response.content)
        return None