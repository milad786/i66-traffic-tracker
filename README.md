I-66 Traffic Pattern Tracker

A project I built to track real-time traffic conditions on I-66 in Northern Virginia, using a live traffic API and a Python data pipeline I put together from scratch.

What it does

The script pulls real-time speed data from the TomTom Traffic API for a point on I-66, calculates whether the road is congested compared to normal free-flow speed, and saves each reading to a local SQLite database. It runs automatically every 5 minutes, so over time it builds up a real dataset of how traffic actually behaves throughout the day.

I let it run for about 15 hours straight and collected 248 readings, which was enough to clearly see rush hour show up in the data.

Tech stack
Python – core language for everything
SQLite – local database for storing readings
TomTom Traffic API – source of real-time traffic data
matplotlib – for charting the results
Git/GitHub – version control
How it works
get_traffic.py calls the TomTom API for a specific point on I-66, pulls out the current speed, free-flow speed, and confidence score, and figures out if the road is congested.
database.py creates the SQLite database and handles saving each reading using parameterized SQL (safe from SQL injection).
A loop with time.sleep() runs the whole process every 5 minutes automatically.
queries.py has the SQL queries I used to analyze the data once I had enough of it.
What I found

Out of 248 readings collected overnight into the next day:

About 17% of readings showed congestion
The worst reading was 13 km/h against a normal free-flow speed of 82 km/h
Congestion was concentrated in a clear window from about 2 PM to 7 PM, with the worst point around 3 PM

Here's what that looks like charted out:

<img width="640" height="480" alt="traffic_chart" src="https://github.com/user-attachments/assets/9e9ef937-f720-4d5f-93f7-862a6c8e04f9" />
