import requests
from bs4 import BeautifulSoup

r = requests.get('https://classroom.btu.edu.ge/ge/student/me/index/3',)

c = r.text
soup = BeautifulSoup(c,'html.parser')

data = soup.find_all('tbody')
print(soup)
