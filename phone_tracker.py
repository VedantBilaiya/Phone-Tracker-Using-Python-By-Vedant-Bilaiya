import phonenumbers

# Write your number with your country code
number = ""

# Tracking PhoneNumbers Country
from phonenumbers import geocoder
county_name = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(county_name,"en"))

# Tracking PhoneNumbers Sim Card Name 
from phonenumbers import carrier
sim_name = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(sim_name,"en"))
