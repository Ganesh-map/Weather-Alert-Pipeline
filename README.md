# 🌦 Real-Time Weather Alerts with Airtable + GitHub Automation

This project pulls **real-time weather data** for major cities (including **Mumbai**) using the **OpenWeatherMap API**, loads the data into **Airtable**, and automatically sends you **daily email alerts** using Airtable's native automation.

---

## ⚙️ How It Works

### 1. **Weather Data Fetch (Python Script)**
- Uses OpenWeatherMap API to fetch weather data for 10 major Indian cities.
- Data includes: temperature, humidity, wind speed, weather condition, and custom alert flags.
- Script runs daily via GitHub Actions (cron job).
- Outputs data to Airtable using Airtable API.

### 2. **Airtable Storage**
- Base: `Weather Alerts`
- Table: `Weather Reports`
- View: `Grid 1` (all data), `Grid 2` (filtered alerts)
- Airtable Formula Field: `Message` – stores a formatted string for each city’s report.

### 3. **Email Automation via Airtable**
- Daily email is triggered every morning.
- Uses Airtable Automation: 
  - **Trigger**: Scheduled time (e.g., 8:15 AM)
  - **Action 1**: Find record where City = Mumbai
  - **Action 2**: Send email with the `Message` field.
- Message contains weather summary with alert condition emojis.

---

## 🧩 Tech Stack

- Python 3
- GitHub Actions (cron job)
- Airtable API
- OpenWeatherMap API
- Airtable Automations
- Gmail

---

## 📨 Sample Email Output

📍 Mumbai - ✅ Normal
🌡️ Temp: 28°C
💧 Humidity: 72%
🌬️ Wind: 10 km/h
🌤️ Condition: Clear Sky


##Author
Made with ✨ and a lots of trial & error by Ganesh Khankal  
🔗 [LinkedIn](www.linkedin.com/in/ganesh-khankal) • 🐙 [GitHub](https://github.com/Ganesh-map)
