import requests
import json

api_key = os.environ['WEATHER_API_KEY']
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
res = requests.get(complete_url)
x = res.json()

if x['cod'] != "404":
    y = x['main']
    current_temperature = y['temp']
    current_temperature_celcius = str(round(current_temperature - 273))
    current_pressure = y['pressure']
    current_humidity = y['humidity']
    z = x['weather']
    weather_description = z[0]['description']
    print(f"Weather Description : {weather_description.title()}")
    print(f"Temperature (C) : {current_temperature_celcius}°C")
    print(f"Temperature (K) : {current_temperature} K")
    print(f"Atmospheric Pressure (hPa) : {current_pressure}")
    print(f"Humidity (%) : {current_humidity}")
else:
    print("404")
