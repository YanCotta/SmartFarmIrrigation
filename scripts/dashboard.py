import sqlite3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect('irrigation.db')

# Load data with formatted timestamp
df = pd.read_sql_query("SELECT id, humidity, phosphorus, potassium, ph, pump_state, strftime('%Y-%m-%d %H:%M:%S', timestamp) as timestamp FROM irrigation_data", conn)

# Dashboard title
st.title("Smart Irrigation Dashboard")

# Plot humidity
st.subheader("Soil Humidity")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['humidity'], 'b-')
ax.set_xlabel("Time")
ax.set_ylabel("Humidity (%)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Plot pH
st.subheader("Soil pH")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['ph'], 'g-')
ax.set_xlabel("Time")
ax.set_ylabel("pH")
plt.xticks(rotation=45)
st.pyplot(fig)

# Plot pump state
st.subheader("Pump State")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['pump_state'], 'r-')
ax.set_xlabel("Time")
ax.set_ylabel("Pump (0=Off, 1=On)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Display raw data table
st.subheader("Raw Data")
st.write(df)

conn.close()