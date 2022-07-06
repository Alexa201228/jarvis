import requests

from offline_functions import greet_user
from online_functions import get_weather_report, find_my_ip, get_trending_films
from speech_engine import speak
from speech_recog_module import take_user_input

if __name__ == '__main__':
    greet_user()
    while True:
        try:
            query = take_user_input().lower()
            if "погода" in query:
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen miss.")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

            elif "фильмы" in query:
                trending_movies = get_trending_films()
                speak("Popular movies today")
                speak(trending_movies)

            elif "спасибо" in query:
                speak("Happy to serve, miss")
                break
        except:
            continue

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
