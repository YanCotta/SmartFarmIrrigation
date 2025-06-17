import sqlite3
import random
from datetime import datetime, timedelta
from database import create_data

# Connect to the irrigation.db database
conn = sqlite3.connect('../irrigation.db')

print("Starting database population with 200 synthetic records...")

# Generate 200 realistic synthetic data records
for i in range(200):
    # Generate realistic sensor values
    humidity = round(random.uniform(20.0, 80.0), 1)  # Humidity 20-80%
    phosphorus = random.choice([0, 1])  # Binary presence
    potassium = random.choice([0, 1])   # Binary presence
    ph = round(random.uniform(4.0, 9.0), 1)  # pH range 4-9
    
    # Determine pump state based on logical rule
    # Pump ON if: humidity < 50 AND 6 <= pH <= 7
    pump_state = 1 if (humidity < 50 and 6.0 <= ph <= 7.0) else 0
    
    # Generate random confidence and model version
    prediction_confidence = round(random.uniform(0.85, 0.99), 3)
    model_version = "v1.0"
    
    # Insert data using the create_data function
    create_data(humidity, phosphorus, potassium, ph, pump_state, 
                prediction_confidence, model_version)
    
    if (i + 1) % 50 == 0:  # Progress indicator
        print(f"Inserted {i + 1} records...")

print("Database population completed! 200 records inserted.")
conn.close()
