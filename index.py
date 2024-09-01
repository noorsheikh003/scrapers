import requests
from bs4 import BeautifulSoup
import pandas as pd

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
            
        rating=row.find('div', class_='t4s-product-price')

        data.append(quote)

df = pd.DataFrame(data)

print(df)
# df.to_csv('heritage_jewels_best_sellers2.csv', index=False)

# print("Data written to heritage_jewels_best_sellers.csv")
