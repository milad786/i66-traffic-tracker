import sqlite3

connection = sqlite3.connect("traffic_data.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic_readings(
               ID INTEGER PRIMARY KEY,
               timestamp CHAR(20),
               current_speed INT,
               free_flow_speed INT,
               confidence DECIMAL (7,2),
               is_congested INT
)
""")

connection.commit()
connection.close()
