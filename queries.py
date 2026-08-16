import sqlite3
import matplotlib.pyplot as plt

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

hours = []
speed = []

for row in results:
    hours.append(row[0])
    speed.append(row[1])

print(hours)
print(speed)


plt.plot(hours, speed)
plt.xlabel("Hour of Day")
plt.ylabel("Average Speed (km/h)")
plt.title("I-66 Traffic Speed by Hour")
plt.savefig("traffic_chart.png")

connection.close()