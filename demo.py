import phonenumbers
import folium 
import opencage

from phonenumbers import geocoder
from myphone import number

pepnum = phonenumbers.parse(number)
location =geocoder.description_for_number(pepnum,"en")
print(location)

from phonenumbers import carrier
spnum=phonenumbers.parse(number)
print(carrier.name_for_number(spnum,"en"))

from opencage.geocoder import OpenCageGeocode

key = '71febcba40cb41e28399a74dc27c1d1d'

geocoder=OpenCageGeocode(key)

query=str(location)
result=geocoder.geocode(query)
#print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']

print(lat,lng)

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng] , popup=location).add_to(mymap)

mymap.save("mylocation.html")