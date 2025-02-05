import requests
import pandas as pd
import matplotlib.pyplot as plt

# WeatherMap API Key 
API_KEY = "b7d2236616c14507b7262117250502"
BASE_URL = "https://www.weatherapi.com/my/"

# List of cities to check weather for
cities = ["New York", "London", "Tokyo", "Paris", "Delhi"]

# Function to fetch weather data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"],
        }
    else:
        print(f"Failed to fetch weather for {city}")
        return None

# Fetch weather data for all cities
weather_data = [get_weather(city) for city in cities]
weather_data = [data for data in weather_data if data]  # Remove failed requests

# Create DataFrame
df = pd.DataFrame(weather_data)

# Display DataFrame
print(df)

# Plot Bar Chart of Temperatures
plt.figure(figsize=(8, 5))
plt.bar(df["City"], df["Temperature"], color=["blue", "green", "red", "orange", "purple"])
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperatures in Different Cities")
plt.show()

# Find Hottest and Coldest City
hottest_city = df.loc[df["Temperature"].idxmax()]
coldest_city = df.loc[df["Temperature"].idxmin()]

print(f"Hottest City: {hottest_city['City']} with {hottest_city['Temperature']}°C")
print(f"Coldest City: {coldest_city['City']} with {coldest_city['Temperature']}°C")


