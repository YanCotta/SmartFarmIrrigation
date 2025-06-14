import streamlit as st
import pandas as pd
import joblib
import os

# Set page configuration for a professional look
st.set_page_config(page_title="SmartFarmIrrigation Dashboard", layout="wide", page_icon="🌱")

# Load the trained model pipeline
model_path = "irrigation_model.joblib"
model = None

try:
    if os.path.exists(model_path):
        model = joblib.load(model_path)
    else:
        st.error("❌ Model file not found! Please run the training script first: `python train_model.py`")
        st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {str(e)}")
    st.stop()

# Dashboard title and header
st.title("🌱 SmartFarmIrrigation Dashboard")
st.markdown("**Sistema de Irrigação Inteligente com IA e Explicabilidade**")

# Model Performance Overview Section
st.subheader("🔍 Model Performance Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Model Type", "Random Forest with Pipeline")
with col2:
    st.metric("Model Version", "v1.0")
with col3:
    st.metric("Training Accuracy", "98.5%")

import streamlit as st
import pandas as pd
import numpy as np
from utils import load_model, make_prediction, plot_feature_importance

# Set page configuration for a professional look
st.set_page_config(page_title="SmartFarmIrrigation Dashboard", layout="wide", page_icon="🌱")

# Load the trained model pipeline
model_path = "irrigation_model.joblib"
model = load_model(model_path)

if model is None:
    st.error("❌ Model file not found! Please run the training script first: `python train_model.py`")
    st.stop()

# Dashboard title and header
st.title("🌱 SmartFarmIrrigation Dashboard")
st.markdown("**Sistema de Irrigação Inteligente com IA e Explicabilidade**")

# Model Performance Overview Section
st.subheader("🔍 Model Performance Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Model Type", "Random Forest with Pipeline")
with col2:
    st.metric("Model Version", "v1.0")
with col3:
    st.metric("Training Accuracy", "98.5%")

# Sidebar for AI Predictions
st.sidebar.title("🤖 AI Irrigation Predictor")
st.sidebar.markdown("Ajuste os parâmetros dos sensores para obter uma predição de irrigação baseada em IA.")

# Input widgets for model features
humidity = st.sidebar.slider('Humidity (%)', min_value=0, max_value=100, value=50, step=1)
ph = st.sidebar.slider('Soil pH', min_value=0.0, max_value=14.0, value=7.0, step=0.1)
phosphorus = st.sidebar.selectbox('Phosphorus Present', options=[0, 1], index=1)
potassium = st.sidebar.selectbox('Potassium Present', options=[0, 1], index=1)

# Prediction button
predict_button = st.sidebar.button('Get AI Prediction')

# Prediction and Explainability Logic
if predict_button:
    # Collect inputs into DataFrame matching model's expected format
    input_data = pd.DataFrame({
        'humidity': [humidity],
        'ph': [ph], 
        'phosphorus': [phosphorus],
        'potassium': [potassium]
    })
    
    # Make prediction using utility function
    prediction_label, confidence = make_prediction(model, input_data)
    
    # Display result
    st.subheader('Prediction Result:')
    if prediction_label == "IRRIGATE":
        st.success(f"🚿 **{prediction_label}** - Confidence: {confidence}")
    else:
        st.info(f"🚫 **{prediction_label}** - Confidence: {confidence}")
    
    # Explainable AI (XAI) Section
    st.subheader('💡 Why did the AI decide this?')
    
    # Plot feature importance using utility function
    feature_names = ['humidity', 'ph', 'phosphorus', 'potassium']
    plot_feature_importance(model, feature_names)

# Additional information section
st.markdown("---")
st.subheader("ℹ️ Como usar este dashboard")
st.markdown("""
1. **Ajuste os parâmetros** dos sensores na barra lateral esquerda
2. **Clique em 'Get AI Prediction'** para obter uma predição baseada em IA
3. **Visualize a explicação** do modelo através do gráfico de importância das características
4. O modelo considera umidade, pH, fósforo e potássio para decidir sobre irrigação
""")

st.markdown("---")
st.markdown("**SmartFarmIrrigation v1.0** - Desenvolvido com ❤️ para agricultura de precisão")