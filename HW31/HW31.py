import requests
import random

def get_website_info(url):
    response = requests.get(url)
    status_code = response.status_code
    website_name = url.split('//')[1].split('/')[0]
    html_length = len(response.text)
    return status_code, website_name, html_length

websites = [
    "https://google.com",
    "https://facebook.com",
    "https://twitter.com",
    "https://amazon.com",
    "https://apple.com"
]

random_website = random.choice(websites)

status_code, website_name, html_length = get_website_info(random_website)

print("Website:", website_name)
print("Status Code:", status_code)
print("HTML Length:", html_length)

city = input("Введіть назву міста: ")

geocoding_url = "https://api.open-meteo.com/v1/forecast/geocode"
geocoding_params = {"location": city}
geocoding_response = requests.get(geocoding_url, params=geocoding_params)
geocoding_data = geocoding_response.json()

if "lat" in geocoding_data and "lon" in geocoding_data:
    latitude = geocoding_data["lat"]
    longitude = geocoding_data["lon"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {"latitude": latitude, "longitude": longitude}
    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    if "current_weather" in weather_data:
        current_weather = weather_data["current_weather"]
        print("Поточна погода у місті", city)
        print("Температура:", current_weather["temperature"], "°C")
        print("Вологість:", current_weather["humidity"], "%")
        print("Швидкість вітру:", current_weather["wind_speed"], "м/с")
else:
    print("Неможливо знайти координати для міста", city)