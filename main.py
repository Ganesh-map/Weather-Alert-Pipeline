import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
AIRTABLE_TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = "Weather Reports"

CITIES = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Bengaluru", "Pune", "Hyderabad", "Jaipur", "Surat"]

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    return res.json()

def check_alerts(data):
    temp = data['main']['temp']
    condition = data['weather'][0]['main']
    
    if temp > 40:
        return "🔥 Heat Alert"
    elif condition in ['Rain', 'Thunderstorm']:
        return "⛈️ Weather Alert"
    else:
        return "✅ Normal"

def upload_to_airtable(records):
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }

    for record in records:
        data = {
            "fields": {
                "City": record["city"],
                "Temperature (°C)": record["temperature"],
                "Condition": record["condition"],
                "Humidity (%)": record["humidity"],
                "Wind Speed (km/h)": record["wind_speed"],
                "Alert": record["alert"],
                "Timestamp": record["timestamp"]
            }
        }
        res = requests.post(url, json=data, headers=headers)
        if res.status_code == 200:
            print(f"✅ Uploaded: {record['city']}")
        else:
            print(f"❌ Failed to upload {record['city']}: {res.text}")

# ========== MAIN FLOW ==========

all_data = []

for city in CITIES:
    data = get_weather(city)
    alert = check_alerts(data)
    
    city_data = {
        "city": city,
        "temperature": data['main']['temp'],
        "condition": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
        "alert": alert,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    all_data.append(city_data)

    # Print to terminal
    status = "🚨" if alert != "✅ Normal" else "✅"
    print(f"{status} {city}: {city_data['condition']} | {city_data['temperature']}°C | {alert}")

# Upload to Airtable
upload_to_airtable(all_data)
