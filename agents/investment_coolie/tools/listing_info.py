import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://partner-stg-api.aspero.co.in/ims/api/v2/listings/?page=1&items=15"

payload = {}
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Authorization': os.getenv('B2B2C_API_KEY'),
  'Current-Entity-Id': os.getenv('B2B2C_API_ENTITY'),
  'channel': os.getenv('B2B2C_API_CHANNEL'),
  'Current-Group': 'distributor',
  'If-None-Match': 'W/"d5716186ee4ba7a4165f3c8af21061f0"',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'X-Request-ID': '6c899ac5-1228-4ac9-9a25-c5bf01c6ad27',
  'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

def get_all_listings():
  print(f"Calling Listings {url}", headers)
  response = requests.request("GET", url, headers=headers, data=payload)
  if response.status_code == 200:
    return response.text
  else:
    print("Failed to fetch data. Status code:", response.status_code, response.content)
    return None
