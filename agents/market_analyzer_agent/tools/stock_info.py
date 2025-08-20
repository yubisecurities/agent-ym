import requests
from urllib.parse import urlencode, quote

import time
import json

# NSE blocks scripts/bots unless headers mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/",
    "Connection": "keep-alive"
}

def get_nse_data(quote_type, symbol_query, symbol):
    # First, get session cookies by visiting homepage.
    session = requests.Session()
    homepage_url = "https://www.nseindia.com/"
    session.get(homepage_url, headers=headers, verify=False)
    time.sleep(2)
    url = f"https://www.nseindia.com/api/{quote_type}?{symbol_query}={quote(symbol)}"
    print(f"Calling NSE {url}")
    response = session.get(url, headers=headers, verify=False)
    if response.status_code == 200:
      return response.text
    else:
      print("Failed to fetch data. Status code:", response.status_code, response.content)
      return None

def get_stock_index(symbol: str) -> dict:
  return get_nse_data('equity-stockIndices', 'index', symbol)

def get_stock(symbol: str) -> dict:
  return get_nse_data('quote-equity', 'symbol', symbol)