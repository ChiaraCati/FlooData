from geopy.geocoders import Nominatim
import pandas as pd
from sympy import false
geolocator = Nominatim(user_agent="FlooData")


doc = pd.read_csv('../datasets/dbf-esempi/Macro_localita_costiere.csv')
#toglie una colonna stupida che faceva da index a caso e senza nome 
doc = doc.drop(doc.columns[0], axis=1)
idx = 0
new_file = pd.DataFrame(columns=['place', 'lat', 'lon'])
for  idx, row in doc.iterrows():
    place = row.NOME 
    location = geolocator.geocode(place)

    if location == None: 
        print(place, 'missing')
        new_file.loc[idx] = [place, 'missing', 'missing']

    else:
        new_file.loc[idx] = [place, location.latitude, location.longitude]

    idx += 1

print(new_file)

new_file.to_csv('../datasets/dbf-esempi/COORDINATES:Macro_localita_costiere.csv', encoding='utf-8')
new_file.to_json('../datasets/dbf-esempi/COORDINATES_Macro_localita_costiere.json')