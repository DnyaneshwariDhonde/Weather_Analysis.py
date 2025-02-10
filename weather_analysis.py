import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "478a8dd048f49049c939d8dde4fa929d"

cities = ["New York", "London", "Tokyo", "Mumbai", "Sydney","pune"]

weather_data = []

for city in cities:
    url = f"http://weatherapi.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"]
        }
        weather_data.append(weather)
    else:
        print(f"Error fetching data for {city}: {response.json()}")


df = pd.DataFrame(weather_data)

print("\nWeather Data:")
display(df)

plt.figure(figsize=(10, 6))
plt.bar(df["City"], df["Temperature"], color="skyblue")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperatures of Cities")
plt.xticks(rotation=45)
plt.show()

max_temp_city = df.loc[df["Temperature"].idxmax()]
min_temp_city = df.loc[df["Temperature"].idxmin()]

print(f"\n The hottest city is {max_temp_city['City']} with {max_temp_city['Temperature']}°C.")
print(f" The coldest city is {min_temp_city['City']} with {min_temp_city['Temperature']}°C.")
