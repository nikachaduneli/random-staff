import requests
from bs4 import BeautifulSoup
r = requests.get('https://top.ge')
c =  r.text

soup = BeautifulSoup(c,'html.parser')
tabledata = soup.find('tbody')

rows = tabledata.find_all('tr')

for index,row in enumerate(rows,1):
    columns = row.find_all('td')
    titles = columns[2].find_all('a')
    avarage_stats = columns[-4].find('span')


    print(f'{str(index)}.{titles[0].text} ({titles[1].text.strip()}), საშულო სტატისტიკა:{avarage_stats.text}')


