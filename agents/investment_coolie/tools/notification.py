import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://platforms-cns-qa-api.myyubiinvest.in/api/v1/notify"

payload = {
  "data": {
    "email": {
      "template": {
        "data": {},
        "name": "trade_approved_to_clients"
      },
      "metadata": {},
      "recipients": {
        "to": [
          "pranavsuresh.priya@yubimarkets.com"
        ]
      }
    },
    "sms": {
      "to": [
        "+919494430527"
      ],
      "from": "CRDAVN",
      "template": {
        "name": "trade_approved_sms",
        "data": {}
      },
      "msgType": "text",
      "priority": "high",
      "principalEntityId": "CredAvenue Private Limited",
      "schedule": "now"
    }
  },
  "version": 1
}
headers = {
  'Accept-Encoding': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + os.getenv('CNS_API_KEY'),
}

def notify(name: str, email: str, phone: str, isin: str, security_name: str, units: str, ytm: str, total_consideration: str) -> dict:
  payload["data"]["email"]["recipients"]["to"].append(email)
  payload["data"]["sms"]["to"].append("+91" + phone)
  template_data = {
    "distributor_name": name,
    "entity_name": name,
    "customer_name": name,
    "trade_id": "TBD",
    "trade_date": "TBD",
    "isin": isin,
    "security_name": security_name,
    "units": units,
    "units_traded": units,
    "yield": ytm,
    "trade_ytm": ytm,
    "total_consideration": total_consideration,
  }
  payload["data"]["email"]["template"]["data"] = template_data
  payload["data"]["sms"]["template"]["data"] = template_data
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
  if response.status_code == 200:
    return response.text
  else:
    print("Failed to fetch data. Status code:", response.status_code, response.content)
    return None