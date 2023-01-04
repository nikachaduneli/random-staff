import requests
from  bs4 import BeautifulSoup

r = requests.get('https://www.worldometers.info/coronavirus/')

data = BeautifulSoup(r.text,'html.parser')

rows = iter(data.find_all('tr'))

i = 0

while i <10:   
  country = next(rows)
  if  country.find('a', {'class':'mt_a'}) is not None:
    i+=1
    name = country.find('a', {'class':'mt_a'}).text
    total_tests = country.find_all('td')[12].text
    print(f'{i}. {name} - {total_tests}')
  