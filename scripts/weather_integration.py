import requests
import sqlite3

# OpenWeather API configuration (replace with your key)
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual key from https://openweathermap.org/
CITY = "Sao Paulo,BR"
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
conn = sqlite3.connect('../irrigation.db')
cursor = conn.cursor()
cursor.execute("SELECT humidity, phosphorus, potassium, ph FROM irrigation_data ORDER BY id DESC LIMIT 1")
humidity, phosphorus, potassium, ph = cursor.fetchone()

# Adjusted irrigation logic with weather
irrigate = (humidity < 50 and phosphorus and potassium and 6 <= ph <= 7 and rain < 1)

# Output results
print(f"Rain: {rain}mm | Humidity: {humidity}% | Phosphorus: {phosphorus} | Potassium: {potassium} | pH: {ph}")
print(f"Irrigate? {'Yes' if irrigate else 'No'}")

conn.close()