import multiprocessing
import threading
import requests

api_key = "0c3a23b3418374fa864f71bcf3d5e018"
cities = ["Kyiv", "Szczecin", "Tampa", "Pafos", "Toronto"]

def get_temperature(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    if "main" in weather_data and "temp" in weather_data["main"]:
        temperature = round(weather_data["main"]["temp"] - 273.15, 1)
        return (city, temperature)
    else:
        return (city, None)

results = []

def threaded_function(city):
    result = get_temperature(city)
    results.append(result)

def multiprocessing_function(city):
    result = get_temperature(city)
    results.append(result)

if __name__ == "__main__":
    threads = []
    for city in cities:
        t = threading.Thread(target=threaded_function, args=(city,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Результати виконання за допомогою мультипотоковості:")
    for result in results:
        print(f"{result[0]}: {result[1]}°C")

    processes = []
    for city in cities:
        p = multiprocessing.Process(target=multiprocessing_function, args=(city,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Результати виконання за допомогою мультипроцесорності:")
    for result in results:
        print(f"{result[0]}: {result[1]}°C")

    temperatures = [result[1] for result in results if result[1] is not None]
    if len(temperatures) > 0:
        max_temp = max(temperatures)
        hottest_city = [result[0] for result in results if result[1] == max_temp][0]
        print(f"У місті {hottest_city} зараз найбільша температура: {max_temp}°C")
    else:
        print("Не вдалося отримати дані про темаратуру")