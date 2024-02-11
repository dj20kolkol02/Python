import requests
import json

def get_weather(api_key, city, units='metric', forecast=False):
    base_url = "https://api.openweathermap.org/data/2.5/"
    endpoint = "forecast" if forecast else "weather"
    
    try:
        response = requests.get(
            f"{base_url}{endpoint}?q={city}&units={units}&appid={api_key}"
        )
        response.raise_for_status()  
        weather_data = response.json()
        
        return weather_data
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_json(data):
    print(json.dumps(data, indent=2))

def main():
    api_key = "f4d9908fde7ce7a97cba51c2a0283dd1"  
    display_option = input("Czy chcesz zobaczyć surowe dane JSON? (Tak/Nie): ").lower()
    city = input("Podaj nazwę miasta: ")
    
    try:
       
        
        if display_option == 'tak':
            option = int(input("Wybierz opcję:\n1. Aktualna pogoda\n2. Pogoda na jutro\nWybór: "))
            if option == 1:
                weather_data = get_weather(api_key, city)
                display_json(weather_data)
                print(f"Aktualna pogoda w {city}: {weather_data['weather'][0]['main']}, temperatura: {weather_data['main']['temp']}°C")
            elif option == 2:
                forecast_data = get_weather(api_key, city, forecast=True)
                display_json(forecast_data)
                print(f"Pogoda na jutro w {city}: {forecast_data['list'][0]['weather'][0]['main']}, temperatura: {forecast_data['list'][0]['main']['temp']}°C")
            else:
                print("Nieprawidłowy wybór.")
                return
        elif display_option == 'nie':
            option = int(input("Wybierz opcję:\n1. Aktualna pogoda\n2. Pogoda na jutro\nWybór: "))
            if option == 1:
                weather_data = get_weather(api_key, city)
                print(f"Aktualna pogoda w {city}: {weather_data['weather'][0]['main']}, temperatura: {weather_data['main']['temp']}°C")
            elif option == 2:
                forecast_data = get_weather(api_key, city, forecast=True)
                print(f"Pogoda na jutro w {city}: {forecast_data['list'][0]['weather'][0]['main']}, temperatura: {forecast_data['list'][0]['main']['temp']}°C")
            else:
                print("Nieprawidłowy wybór.")
                return
        else:
            print("Nieprawidłowa opcja. Wybierz 'Tak' lub 'Nie'.")
            return
    
    except ValueError:
        print("Wprowadź prawidłową liczbę.")
        return
    
    
if __name__ == "__main__":
    main()
