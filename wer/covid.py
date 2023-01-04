import requests
import json

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

querystring = {"country":"Georgia"}

headers = {
    'x-rapidapi-key': "3a9f482358msh9b43ab58fcce78bp1e7547jsn133a625dfe0b",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
all_ata = json.loads(response.text)
data = all_ata['data']


print(f'death: {data["deaths"]}')
print(f'confirmed: {data["confirmed"]}')

print(f'location: {data["location"]}')
import requests

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt2560140"

headers = {
    'x-rapidapi-key': "3a9f482358msh9b43ab58fcce78bp1e7547jsn133a625dfe0b",
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)