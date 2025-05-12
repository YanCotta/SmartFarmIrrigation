import requests
import sqlite3

API_KEY = "SUA_CHAVE_API_AQUI"  # Substitua pela sua chave
CITY = "Sao Paulo,BR"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Obter dados climáticos
response = requests.get(URL).json()
rain = response.get('rain', {}).get('1h', 0)  # Chuva em 1h (mm)

# Conectar ao banco
conn = sqlite3.connect('irrigation.db')
cursor = conn.cursor()
cursor.execute("SELECT humidity, phosphorus, potassium, ph FROM irrigation_data ORDER BY id DESC LIMIT 1")
humidity, phosphorus, potassium, ph = cursor.fetchone()

# Lógica de irrigação ajustada
irrigate = (humidity < 50 and phosphorus and potassium and 6 <= ph <= 7 and rain < 1)

print(f"Chuva: {rain}mm | Umidade: {humidity}% | Fósforo: {phosphorus} | Potássio: {potassium} | pH: {ph}")
print(f"Irrigar? {'Sim' if irrigate else 'Não'}")

conn.close()