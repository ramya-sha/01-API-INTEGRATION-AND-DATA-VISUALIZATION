import requests
import matplotlib.pyplot as plt
url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=13.0827&longitude=80.2707"
    "&current_weather=true"
)
response = requests.get(url)
data = response.json()
temperature = data["current_weather"]["temperature"]
windspeed = data["current_weather"]["windspeed"]
winddirection = data["current_weather"]["winddirection"]
print("Current Weather in Chennai")
print("Temperature:", temperature, "°C")
print("Wind Speed:", windspeed, "km/h")
print("Wind Direction:", winddirection, "°")
labels = ["Temperature (°C)", "Wind Speed (km/h)", "Wind Direction (°)"]
values = [temperature, windspeed, winddirection]
plt.figure()
plt.bar(labels, values)
plt.title("Live Weather Data Visualization - Chennai")
plt.show()
