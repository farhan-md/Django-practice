import requests

api_key = "0b5e259d1391acedcd3d15fd45bca6ac"

city = input("Enter the city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

try:
    weather = requests.get(url).json()
    main = weather["weather"][0]["main"]
    description = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]

    print(f"city name: {city}")
    print(f"weather status: {main}")
    print(f"weather description: {description}")
    print(f"weather temporator: {temp}")

except:
    print("Connection Error")
