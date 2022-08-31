'''
MIT License (MIT)
Copyright © 2022 Chiara Catizone, Giulia Venditti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

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