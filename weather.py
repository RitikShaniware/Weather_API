import requests

def get_weather_data(city_name):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city_name}&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from the API.")
        return None

def get_temperature(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['main']['temp']
    return None

def get_wind_speed(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['wind']['speed']
    return None

def get_pressure(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['main']['pressure']
    return None

def main():
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name)

    if weather_data is None:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting the program...")
            break
        elif choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
