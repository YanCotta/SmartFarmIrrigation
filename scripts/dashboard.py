import sqlite3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Set page configuration for a professional look
st.set_page_config(page_title="SmartFarmIrrigation Dashboard", layout="wide", page_icon="🌱")

# OpenWeather API configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual key
CITY = "Sao Paulo,BR"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Connect to database
conn = sqlite3.connect('irrigation.db')

# Load data
df = pd.read_sql_query("SELECT id, humidity, phosphorus, potassium, ph, pump_state, strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp FROM irrigation_data", conn)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sidebar for filters
st.sidebar.title("Filtros do Dashboard")
st.sidebar.markdown("Ajuste os parâmetros para explorar os dados.")

# Date range filter
min_date = df['timestamp'].min()
max_date = df['timestamp'].max()
start_date = st.sidebar.date_input("Data Inicial", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("Data Final", max_date, min_value=min_date, max_value=max_date)

# Filter dataframe
filtered_df = df[(df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)]

# Dashboard title and header
st.title("🌱 SmartFarmIrrigation Dashboard")
st.markdown("**Monitoramento em tempo real de irrigação inteligente para agricultura de precisão**")

# Metrics row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Umidade Média", f"{filtered_df['humidity'].mean():.1f}%")
with col2:
    st.metric("pH Médio", f"{filtered_df['ph'].mean():.1f}")
with col3:
    st.metric("Bomba Ativa", f"{filtered_df['pump_state'].sum()} vezes")

# Weather-based irrigation decision
st.subheader("Decisão de Irrigação Baseada no Clima")
try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    rain = data.get('rain', {}).get('1h', 0)
except:
    rain = 0.5  # Mock value if API fails

latest = filtered_df.iloc[-1] if not filtered_df.empty else pd.Series({'humidity': 50, 'phosphorus': 0, 'potassium': 0, 'ph': 7})
irrigate = (latest['humidity'] < 50 and latest['phosphorus'] and latest['potassium'] and 6 <= latest['ph'] <= 7 and rain < 1)
st.write(f"**Irrigar? {'Sim' if irrigate else 'Não'}** (Chuva recente: {rain}mm)")

# Plots
st.subheader("Gráficos de Monitoramento")
col1, col2 = st.columns(2)

# Humidity plot
with col1:
    st.markdown("**Umidade do Solo**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(filtered_df['timestamp'], filtered_df['humidity'], 'b-', label='Umidade (%)')
    ax.set_xlabel("Data/Hora")
    ax.set_ylabel("Umidade (%)")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# pH plot
with col2:
    st.markdown("**pH do Solo**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(filtered_df['timestamp'], filtered_df['ph'], 'g-', label='pH')
    ax.set_xlabel("Data/Hora")
    ax.set_ylabel("pH")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Pump state plot
st.markdown("**Estado da Bomba**")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered_df['timestamp'], filtered_df['pump_state'], 'r-', label='Bomba (0=Desligada, 1=Ligada)')
ax.set_xlabel("Data/Hora")
ax.set_ylabel("Estado")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Raw data table
st.subheader("Dados Brutos")
st.dataframe(filtered_df[['id', 'timestamp', 'humidity', 'phosphorus', 'potassium', 'ph', 'pump_state']], use_container_width=True)

conn.close()