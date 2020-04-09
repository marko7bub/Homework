import urllib.request
import json

# Enter the name of your movie
inp = input('Enter movie name: ')
BASE_URL = "http://omdbapi.com/?t={}&apikey=52c58877".format(
    '+'.join(inp.split()))
f = urllib.request.urlopen(BASE_URL)
data = json.loads(f.read())
# Get some information about your movie
print('The name of your movie is ' + data['Title'])
print('It was released on ' + data['Released'])
print('It was directed by ' + data['Director'])
print('The story is: ' + data['Plot'])
