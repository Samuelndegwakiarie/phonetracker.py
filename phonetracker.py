import phonenumbers
from test import number 
from phonenumbers import geocoder

# Assuming 'number' is a valid phone number in international format
number = "+254720733677"
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number, "en"))
