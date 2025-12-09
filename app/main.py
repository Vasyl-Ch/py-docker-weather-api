import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    CITY = "Paris"
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")
    WEATHER_API_URL  = "https://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": CITY}
    response = requests.get(WEATHER_API_URL , params=params)
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
