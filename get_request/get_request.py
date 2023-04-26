import requests
city_name = input("Enter the city name :-")
tocken = '92bd5ed0fd962d92d7f36453b5a27995'
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={tocken}"
a = str(requests.get(url).status_code)
print("Status code is :- "+a)
b = requests.get(url).json()
print(len(b))
if len(b) == 0:
    print("Their is no city name in our world.")
else:
    lat = str(b[0]['lat'])
    lon = str(b[0]['lon'])
    country = str(b[0]['country'])
    print("City name is " + city_name, "and their lat is " + lat, "and lon is " + lon)
    print("Country name is "+country)
if b[0]['local_names'].get('hi',None):
    print("City name in hindi is "+b[0]['local_names']['hi'])
else:
    print("Their is no name in hindi of this city.")
