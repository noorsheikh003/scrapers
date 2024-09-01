import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

URL = 'https://heritagejewels.com.pk/'
r = requests.get(URL)

data = []
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('div', attrs={'data-collection-url': '/collections/best-sellers'})

if table:
    for row in table.findAll('div', attrs={"class": "t4s-product-info__inner"}):
        quote = {}
        quote['name'] = row.find('h3', class_='t4s-product-title').text.strip()

        price_div = row.find('div', class_='t4s-product-price')
        if price_div:
            quote['price'] = price_div.text.strip()
        else:
            quote['price'] = 'Price not found'
    
        quote['rating']=row.find('span', class_="jdgm-prev-badge__text").text.strip().replace("reviews", '')
        

        data.append(quote)

df = pd.DataFrame(data)

current_time = str(datetime.datetime.now())

df.to_csv('file_' + current_time + '.csv', index=False)

print("Data written to heritage_jewels_best_sellers.csv")
