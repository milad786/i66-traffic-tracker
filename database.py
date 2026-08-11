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

def save_reading(timestamp, current_speed, free_flow_speed, confidence, is_congested):
    connection = sqlite3.connect("traffic_data.db")
    cursor = connection.cursor()

    cursor.execute("""
                INSERT INTO traffic_readings(timestamp, current_speed, free_flow_speed, confidence, is_congested)
                    VALUES (?,?,?,?,?)
    """, (
        timestamp, current_speed, free_flow_speed, confidence, is_congested
    ))

    connection.commit()
    connection.close()

save_reading("2026-08-11 14:30:00", 45, 80, 1.0, True)