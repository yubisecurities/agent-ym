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
  'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoMHw2NmNkYjQzMDRlNGYyYmYwY2NhM2ZkNDkiLCJpc3MiOiJodHRwczovL2F1dGgtcWEubXl5dWJpaW52ZXN0LmluLyIsImlhdCI6MTc1NTcxNjEzMywiYXVkIjoiaHR0cHM6Ly9hdXRoLXFhLWFwaS5teXl1YmlpbnZlc3QuaW4iLCJleHAiOjE3NTU3MjMzMzMsImh0dHBzOi8vYXV0aC1xYS1hcGkubXl5dWJpaW52ZXN0LmluL2xvY2FsX3VzZXJfaWQiOiI2NmNkYjQzMDIwMWMxZDAwNjBiODcyZWMiLCJodHRwczovL2F1dGgtcWEtYXBpLm15eXViaWludmVzdC5pbi9lbnRpdHlfaWQiOiI2NTAzZjIzY2Y4ZjBmMTAwNjFlMTFiMWEiLCJodHRwczovL2F1dGgtcWEtYXBpLm15eXViaWludmVzdC5pbi9ncm91cHMiOlsiZGlzdHJpYnV0b3IiXSwiaHR0cHM6Ly9hdXRoLXFhLWFwaS5teXl1YmlpbnZlc3QuaW4vcm9sZXMiOlsiYWRtaW4iXSwiaHR0cHM6Ly9hdXRoLXFhLWFwaS5teXl1YmlpbnZlc3QuaW4vc3ViZ3JvdXBzIjpbXSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImh0dHBzOi8vYXV0aC1xYS1hcGkubXl5dWJpaW52ZXN0LmluL3NraXBfaHJtcyI6dHJ1ZX0.mn1kGzmQqH4wJK7p8g9Dw3qKqPUROz2HdiGI4Ex_OXU',
  'channel': 'partner',
  'content-type': 'application/json',
  'current-entity-id': '6503f23cf8f0f10061e11b1a',
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