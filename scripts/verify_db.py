import sqlite3
import os

# Get the absolute path to the database
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'irrigation.db')
print(f"Looking for database at: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM irrigation_data")
    count = cursor.fetchone()[0]
    print(f"✅ Database verified! Found {count} records in irrigation_data table")
    
    # Show a sample of the data
    cursor.execute("SELECT * FROM irrigation_data LIMIT 3")
    sample = cursor.fetchall()
    print("Sample data:")
    for row in sample:
        print(f"  ID: {row[0]}, Humidity: {row[1]}%, pH: {row[2]}, Pump: {row[5]}")
    
    conn.close()
    print("✅ Database verification completed successfully!")
    
except sqlite3.Error as e:
    print(f"❌ Database error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")