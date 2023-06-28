import requests
import random

def make_website_request():
    websites = [
        "google.com",
        "facebook.com",
        "twitter.com",
        "amazon.com",
        "apple.com"
    ]

    random_website = random.choice(websites)
    response = requests.get("http://" + random_website)
    status_code = response.status_code
    site_name = random_website
    html_length = len(response.text)

    print("Статус-код:", status_code)
    print("Назва сайту:", site_name)
    print("Довжина HTML-коду:", html_length)

def get_weather(city):
    geocoding_url = "https://api.open-meteo.com/v1/geocode?city=" + city
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()

    if "status" in geocoding_data and geocoding_data["status"] == "OK":
        latitude = geocoding_data["results"][0]["latitude"]
        longitude = geocoding_data["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if "current_weather" in weather_data:
            current_weather = weather_data["current_weather"]
            temperature = current_weather["temperature"]
            humidity = current_weather["humidity"]
            wind_speed = current_weather["wind_speed"]

            print("Температура:", temperature)
            print("Вологість:", humidity)
            print("Швидкість вітру:", wind_speed)
    else:
        print("Помилка при отриманні даних про геокодування")

def main():
    choice = input("Виберіть опцію:\n1. Запит до сайту\n2. Погода\n")

    if choice == "1":
        make_website_request()
    elif choice == "2":
        city = input("Введіть назву міста: ")
        get_weather(city)
    else:
        print("Невірний вибір")

if __name__ == "__main__":
    main()