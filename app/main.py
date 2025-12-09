import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")
    weather_url = "https://api.weatherapi.com/v1/current.json"
    city = "Paris"
    params = {"key": api_key, "q": city}
    response = requests.get(weather_url , params=params)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(
        "Performing request to Weather API for city Paris...\n"
        f"{city}/{country} {time} "
        f"Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
