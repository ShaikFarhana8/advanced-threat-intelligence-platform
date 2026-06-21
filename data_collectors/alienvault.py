import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OTX_API_KEY")

url = "https://otx.alienvault.com/api/v1/users/me"

headers = {
    "X-OTX-API-KEY": API_KEY
}

response = requests.get(url, headers=headers, timeout=10)

print("Status Code:", response.status_code)
print(response.text)