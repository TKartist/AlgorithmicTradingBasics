from phoneNumber import number
import phonenumbers
import opencage
from phonenumbers import geocoder
from api import api_key

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(api_key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat, lng)
