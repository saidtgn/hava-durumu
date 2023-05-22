import requests
import json


#Test initial commit.

def havaDurumu(self):
    sehir = self
    apiKey = 'YOUR_API_KEY'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}')
    
    weatherData = response.json()

    #For clouds: Eng to Turkish Description:
    #Bulut tanımlarını ing den türkçeye çevirir ve skyDescription değişkenine atar.
    skyDescription = weatherData['weather'][0]['description']
    cityName = weatherData['name']
    skyTypes = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']
    skyTypesTR = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    for i in range(len(skyTypes)):
        if skyDescription == skyTypes[i]:
            skyDescription = skyTypesTR[i]

    # Adding test comment for commit.
    #For temp: Kelvin to Celcius:
    #Sıcaklık bilgisini Kelvin den Celcius a çevirir ve aşağıdaki değişkenlerin içine atar.
    temp = round((weatherData['main']['temp'] - 273.15), 2) #Genel sıcaklık
    feels_temp = round((weatherData['main']['feels_like'] - 273.15), 2) #hissedilen
    temp_min = round((weatherData['main']['temp_min'] - 273.15), 2) #Minimum
    temp_max = round((weatherData['main']['temp_max'] - 273.15), 2) #Maksimum

    havadurumudict = {
        "Şehir": cityName,
        "Gökyüzü": skyDescription,
        "Sıcaklık": temp,
        "Hissedilen": feels_temp,
        "Minimum": temp_min,
        "Maksimum": temp_max
    }

    return havadurumudict




if __name__ == "__main__":

    sehirİsmi = "İstanbul"
    print(havaDurumu(sehirİsmi))
