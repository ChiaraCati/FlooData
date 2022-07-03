import urllib
from urllib.request import urlopen

url = 'https://datacatalog.regione.emilia-romagna.it/catalogCTA/api/action/datastore_search?resource_id=1f56dc65-bc60-4e40-875e-d2c56318b034&limit=5&q=title:jones'
fileobj = urlopen(url)
print(fileobj.read())