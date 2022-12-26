from faker import Faker
import pandas as pd
from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent = 'your_app_name')

fake = Faker('pt_BR')

ids = []
cities = []
states = []

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

location = {
    'id': ids,
    'city': cities,
    'state': states,
}

df = pd.DataFrame(location, columns = ['id', 'city', 'state'])
path = '../csvs/locations.csv'
df.to_csv(path_or_buf=path, encoding='utf-8', index=False)