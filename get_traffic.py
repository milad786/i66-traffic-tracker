import os
import requests
from dotenv import load_dotenv
from datetime import datetime
now = datetime.now()
timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
from database import save_reading

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

data = response.json()
flow_data = data["flowSegmentData"]
current_speed = flow_data["currentSpeed"]
free_flow_speed = flow_data["freeFlowSpeed"]
confidence = flow_data['confidence']
is_congested = current_speed < (free_flow_speed * 0.8)



print("Status code:", response.status_code)

print(timestamp_str)

print(current_speed)
print(free_flow_speed)
print(confidence)
save_reading(timestamp_str, current_speed, free_flow_speed, confidence, is_congested)