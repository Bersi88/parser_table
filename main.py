import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table').find_all('tr')
rezult = {key.text : 0 for key in table[0].find_all('th')}
for string in table[1:]:
    row = string.find_all('td')
    for key, val_1 in zip(rezult.items(), row):
        rezult[key[0]] = round(float(val_1.text) + key[1], 3)
print(rezult)
