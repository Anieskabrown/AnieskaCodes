import requests
import json
from datetime import datetime  # Importing datetime for current timestamp


# Here I've used thed 'def' function to fetch weather data from OpenWeatherMap API
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    # I had to check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None  # Return None if the request failed


# Here I used the 'def' function to analyze the weather and provide recommendations I wanted my user to be
# Get the weather and a little extra.
def analyze_weather(data):
    # Check if the API response contains the expected data
    if data is None or 'main' not in data or 'weather' not in data:
        return "Error: Weather data is unavailable. Please check your city name or API key."

    temp = data['main']['temp']  # Extracting temperature in Celsius
    weather_desc = data['weather'][0]['description']  # Extracting weather description

    advice = f"The current temperature is {temp}°C with {weather_desc}.\n"

    # I incorporated boolean logic as recommendations in order to let the user know to use sunscreen or  bring
    # an umbrella if it is raining or its cold to keep warm.
    if temp > 20:
        advice += "It's hot outside! Don't forget to wear sunscreen.\n"

    if 'rain' in weather_desc.lower():
        advice += "It looks like it's raining. Don't forget to bring an umbrella!\n"

    if temp < 10:
        advice += "ooo It's cold out, wrap up warm!\n"


    return advice

# Function to save the weather advice to a file
def save_weather_report(content, city_name, filename="weather_report.txt"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
    with open(filename, "w") as file:
        file.write(f"Weather report for {city_name} generated at {current_time}\n\n")  # Write timestamp
        file.write(content)  # Write the weather content

# Here I wanted to add the function to save favorite city
def save_favorite_city(city_name, filename="favorites.txt"):
    with open(filename, "a") as file:
        file.write(city_name + "\n")  #

def load_favorite_cities(filename="favorites.txt"):
    try:
        with open(filename, "r") as file:
            cities = [line.strip() for line in file.readlines()]
            return cities
    except FileNotFoundError:
        return []

# This is able to print and save the weather information
def process_weather(city_name, api_key):
    weather_data = get_weather(city_name, api_key)
    advice = analyze_weather(weather_data)
    print(advice)  # Print the result
    save_weather_report(advice, city_name)

def main():
    favorites = load_favorite_cities()

    print("Welcome to the Weather App!")
    if favorites:
        print("Your favorite cities:")
        for i, city in enumerate(favorites, 1):
            print(f"{i}. {city}")

        choice = input("Do you want to use a favorite city? Enter the number or 'n' for a new city: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(favorites):
            city_name = favorites[int(choice) - 1]
        else:
            city_name = input("Enter your city name: ").strip()
    else:
        city_name = input("Enter your city name: ").strip()

    save_fav = input(f"Do you want to save {city_name} as a favorite city? (y/n): ").strip().lower()
    if save_fav == 'y':
        save_favorite_city(city_name)
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    process_weather(city_name, api_key)


if __name__ == "__main__":
    main()
