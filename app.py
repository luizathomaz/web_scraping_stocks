import requests 
from bs4 import BeautifulSoup
import csv

url = "https://finance.yahoo.com/most-active"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

all_data = soup.find_all('tr', attrs={'class': 'simpTblRow'})


data = [['Symbol', 'Name', 'Price', 'Change', '% Change', 'Volume', 'Avg Vol (3 month)', 'Market Cap']]
symbol = soup.find_all('a', attrs={'class': 'Fw(600) C($linkColor)'})
name = soup.find_all('td', attrs={'aria-label': 'Name'})
price = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
change = soup.find_all('td', attrs={'aria-label': 'Change'})
perc_change = soup.find_all('td', attrs={'aria-label': '% Change'})
volume = soup.find_all('td', attrs={'aria-label': 'Volume'})
avg_vol = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
market_cap = soup.find_all('td', attrs={'aria-label': 'Market Cap'})

for e in range(0, len(all_data)):
    lista = [symbol[e].text, name[e].text, price[e].text, change[e].text, perc_change[e].text, volume[e].text, avg_vol[e].text, market_cap[e].text]
    data.append(lista)


with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, quotechar='"')
    writer.writerows(data)
