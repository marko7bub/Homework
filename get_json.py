import urllib.request
import json

BASE_URL = "http://omdbapi.com/?t=The+Avengers&y=2012&apikey=52c58877"
f = urllib.request.urlopen(BASE_URL)
data = json.loads(f.read())
print(data)
