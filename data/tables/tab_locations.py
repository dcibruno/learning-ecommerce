from faker import Faker
import pandas as pd
from geopy.geocoders import Nominatim
import random

geocoder = Nominatim(user_agent = 'your_app_name')

fake = Faker('pt_BR')

ids = []
cities = []
states = []
city_tax = []

for row in range(0, 50+1):
    
    ids.append(row)
    
    latlong = fake.local_latlng(country_code='BR')[:2]
    loc = geocoder.reverse((latlong)).raw['address']

    city = loc.get('town', loc.get('suburb', 'Not Found'))
    cities.append(city)

    if city == 'Not Found':
        states.append('Not Found')
    else:
        states.append(loc.get('state'))
    
    city_tax.append(round(random.uniform(0.05, 0.15), 4))

location = {
    'id': ids,
    'city': cities,
    'state': states,
    'city_tax': city_tax
}

df = pd.DataFrame(location, columns = ['id', 'city', 'state', 'city_tax'])
path = '../csvs/locations.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)