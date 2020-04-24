import requests

def get_weather_api(city):
    parameters = {"q": city, "appid": "5a379190bfc2627d0c791dc5ab8565f7"}
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameters)
    description = weather.json()["weather"][0]["description"]
    return description




