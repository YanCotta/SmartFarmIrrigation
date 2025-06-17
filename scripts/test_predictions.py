#!/usr/bin/env python3
"""
Quick test script to validate model predictions work correctly
"""
import pandas as pd
import joblib

# Load the model
model = joblib.load('irrigation_model.joblib')

# Test data in correct order: humidity, phosphorus, potassium, ph
test_cases = [
    {"name": "High Humidity", "humidity": 80, "phosphorus": 1, "potassium": 1, "ph": 7.0},
    {"name": "Low Humidity", "humidity": 30, "phosphorus": 1, "potassium": 1, "ph": 6.5},
    {"name": "Medium Humidity", "humidity": 50, "phosphorus": 0, "potassium": 0, "ph": 7.5}
]

print("=== MODEL PREDICTION TESTS ===")
for test in test_cases:
    # Create DataFrame with correct feature order
    input_data = pd.DataFrame({
        'humidity': [test['humidity']],
        'phosphorus': [test['phosphorus']],
        'potassium': [test['potassium']],
        'ph': [test['ph']]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]
    confidence = prediction_proba[prediction] * 100
    
    result = "IRRIGATE" if prediction == 1 else "DO NOT IRRIGATE"
    
    print(f"\n{test['name']}:")
    print(f"  Input: Humidity={test['humidity']}%, Phosphorus={test['phosphorus']}, Potassium={test['potassium']}, pH={test['ph']}")
    print(f"  Prediction: {result}")
    print(f"  Confidence: {confidence:.1f}%")

print("\n=== Test completed successfully! ===")
