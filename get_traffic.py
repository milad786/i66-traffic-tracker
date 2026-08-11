import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TOMTOM_API_KEY")

LATITUDE = 38.8815
LONGITUDE = -77.2247

url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
params = {
    "key": API_KEY,
    "point": f"{LATITUDE},{LONGITUDE}"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)
print(response.json())
