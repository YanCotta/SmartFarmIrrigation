import sqlite3
import os

# Database configuration
DB_PATH = '../irrigation.db'

def initialize_database():
    """Initialize the database and create tables if they don't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Create table aligned with simplified MER from Fase 2
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS irrigation_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            humidity REAL,          -- Soil humidity percentage
            phosphorus INTEGER,     -- Phosphorus presence (0 or 1)
            potassium INTEGER,      -- Potassium presence (0 or 1)
            ph REAL,                -- Soil pH value
            pump_state INTEGER,     -- Pump state (0 = off, 1 = on)
            prediction_confidence REAL,  -- ML model confidence
            model_version TEXT,     -- Model version used
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()
        print("Table created or already exists.")

# CRUD Functions
def create_data(humidity, phosphorus, potassium, ph, pump_state, prediction_confidence=None, model_version=None):
    """Insert new sensor data into the database."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO irrigation_data (humidity, phosphorus, potassium, ph, pump_state, prediction_confidence, model_version) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (humidity, phosphorus, potassium, ph, pump_state, prediction_confidence, model_version))
        conn.commit()
        print("Data inserted.")

def read_all():
    """Retrieve all data from the irrigation_data table."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM irrigation_data')
        return cursor.fetchall()

def update_data(id, humidity=None, pump_state=None):
    """Update humidity or pump_state for a specific record."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if humidity is not None:
            cursor.execute('UPDATE irrigation_data SET humidity = ? WHERE id = ?', (humidity, id))
        if pump_state is not None:
            cursor.execute('UPDATE irrigation_data SET pump_state = ? WHERE id = ?', (pump_state, id))
        conn.commit()
        print("Data updated.")

def delete_data(id):
    """Delete a specific record by ID."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM irrigation_data WHERE id = ?', (id,))
        conn.commit()
        print("Data deleted.")

# Example usage
if __name__ == "__main__":
    # Initialize database
    initialize_database()
    
    # Insert simulated data
    create_data(45.0, 1, 1, 6.5, 1, 0.95, "v1.0")
    create_data(60.0, 0, 1, 7.2, 0, 0.87, "v1.0")

    # Print stored data
    print("Stored Data:")
    for row in read_all():
        print(row)

    # Update and delete examples
    update_data(1, humidity=50.0)
    delete_data(2)