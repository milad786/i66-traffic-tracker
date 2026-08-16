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

cursor.execute("""
select *
        from traffic_readings
        ORDER BY current_speed ASC
        limit 1
""")

results = cursor.fetchall()
print(results)

cursor.execute("""
select strftime('%H', timestamp) as hour , AVG(current_speed)
        from traffic_readings
        group by hour
""")

results = cursor.fetchall()
print(results)

connection.close()