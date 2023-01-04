import requests
import json

def main():


    icao_iata = input('enter airport icao or iata code: ')
    url = "https://airport-info.p.rapidapi.com/airport"

    querystring = {"icao":icao_iata,"iata":icao_iata}

    headers = {
        'x-rapidapi-key': "3a9f482358msh9b43ab58fcce78bp1e7547jsn133a625dfe0b",
        'x-rapidapi-host': "airport-info.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads((response.text))
    print('\n'*2+"Airport Information")
    for i in data:
        print(f'{i}: {data.get(i)}')


main()
