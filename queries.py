import sqlite3

connection = sqlite3.connect("traffic_data.db")
cursor = connection.cursor()

cursor.execute("""
select is_congested, count(*)
        from traffic_readings
        GROUP BY is_congested
""")

results = cursor.fetchall()
print(results)

connection.close()