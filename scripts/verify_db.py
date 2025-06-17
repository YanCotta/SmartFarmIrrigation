import sqlite3
conn = sqlite3.connect('../irrigation.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM irrigation_data")
print(cursor.fetchall())
conn.close()