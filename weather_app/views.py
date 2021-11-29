from django.shortcuts import render



from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method =='POST':
        city = request.POST['city']
        source=urllib.request.urlopen('api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=3faf733aa760a56c7918e117157e10a7').read()

        list_of_data=json.loads(source)

        data={
            "country_code": str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+','+str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['pressure']),
            "main":str(list_of_data ['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":list_of_data['weather'][0]['icon']
        }
        print(data)
    else:
        data={}
    
   
    return render(request, 'weather_app/index.html',data)