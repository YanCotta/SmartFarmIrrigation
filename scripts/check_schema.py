import sqlite3

# Connect to the database
conn = sqlite3.connect('irrigation.db')
cursor = conn.cursor()

# Check current table schema
print("=== CURRENT TABLE SCHEMA ===")
cursor.execute('PRAGMA table_info(irrigation_data)')
columns = cursor.fetchall()
for col in columns:
    print(f"Column: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")

print("\n=== SAMPLE DATA ===")
cursor.execute('SELECT * FROM irrigation_data LIMIT 3')
sample_data = cursor.fetchall()
for row in sample_data:
    print(row)

conn.close()
