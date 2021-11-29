from django.shortcuts import render



from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method =='POST':
        city = request.POST.get('city','Nairobi')
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=bfd32ae183b959533fe3eda252ddb33f').read()

        list_of_data=json.loads(source)

        data={
            'city':city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+','+str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
        
        }
        print(data)
    else:
        data={}
    
   
    return render(request, 'weather_app/index.html',data)
