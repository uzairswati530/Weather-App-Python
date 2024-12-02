import requests
import json
import os

# User input for the city name
city = input("Enter the name of the city:\n ")

# Weather API URL with the city
url = f"https://api.weatherapi.com/v1/current.json?key=f399f6f371c44bc09b7121903243011&q={city}"

# Make the API request
r = requests.get(url)

if r.status_code == 200:
    wdic = json.loads(r.text)  # Parse JSON response
    w = wdic["current"]["temp_c"]  # Get the temperature in Celsius
    print(f"The current temperature in {city} is {w}°C.")

    # Use PowerShell to read the output aloud (Windows compatible)
    command = f"powershell -Command \"Add-Type -AssemblyName System.Speech; " \
              f"$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; " \
              f"$speak.Speak('The current weather in {city} is {w} degrees')\""
    os.system(command)
else:
    print("Failed to fetch weather data. Please check the city name or API key.")
