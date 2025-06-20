import requests
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# OpenWeather API configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Sao Paulo,BR")  # Default fallback

# Validate API key
if not API_KEY or API_KEY == "YOUR_ACTUAL_API_KEY_HERE":
    print("Warning: Please set your OpenWeather API key in the .env file")
    print("Get your free API key at: https://openweathermap.org/")
    rain = 0  # Default to no rain if API key is not configured
else:
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        # Fetch weather data
        response = requests.get(URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        rain = data.get('rain', {}).get('1h', 0)  # Rainfall in last hour (mm)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        rain = 0  # Default to no rain if API fails

# Connect to database and get latest sensor data
with sqlite3.connect('../irrigation.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT humidity, phosphorus, potassium, ph FROM irrigation_data ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    
    if result:
        humidity, phosphorus, potassium, ph = result
    else:
        print("No data found in database. Using default values.")
        humidity, phosphorus, potassium, ph = 50, 1, 1, 7.0

# Adjusted irrigation logic with weather
irrigate = (humidity < 50 and phosphorus and potassium and 6 <= ph <= 7 and rain < 1)

# Output results
print(f"Rain: {rain}mm | Humidity: {humidity}% | Phosphorus: {phosphorus} | Potassium: {potassium} | pH: {ph}")
print(f"Irrigate? {'Yes' if irrigate else 'No'}")
print(f"Weather Factor: {'No recent rain' if rain < 1 else f'Recent rain: {rain}mm - irrigation not needed'}")

conn.close()