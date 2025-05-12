import sqlite3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Conectar ao banco
conn = sqlite3.connect('irrigation.db')

# Carregar dados
df = pd.read_sql_query("SELECT * FROM irrigation_data", conn)

# Título
st.title("Dashboard de Irrigação Inteligente")

# Gráficos
st.subheader("Umidade do Solo")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['humidity'], 'b-')
ax.set_xlabel("Tempo")
ax.set_ylabel("Umidade (%)")
st.pyplot(fig)

st.subheader("pH do Solo")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['ph'], 'g-')
ax.set_xlabel("Tempo")
ax.set_ylabel("pH")
st.pyplot(fig)

st.subheader("Estado da Bomba")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['pump_state'], 'r-')
ax.set_xlabel("Tempo")
ax.set_ylabel("Bomba (0=Desligada, 1=Ligada)")
st.pyplot(fig)

# Tabela de dados
st.subheader("Dados Brutos")
st.write(df)

conn.close()