import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL = 'https://heritagejewels.com.pk/'
r = requests.get(URL)

data = []
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('div', attrs={'data-collection-url': '/collections/best-sellers'})

if table:
    for row in table.findAll('div', attrs={"class": "t4s-product-info__inner"}):
        quote = {}
        
        # Safely extract the product name
        name_tag = row.find('h3', class_='t4s-product-title')
        quote['name'] = name_tag.text.strip() if name_tag else 'Name not found'

        # Safely extract the product price
        price_div = row.find('div', class_='t4s-product-price')
        quote['price'] = price_div.text.strip() if price_div else 'Price not found'

        # Safely extract the rating
        rating_tag = row.find('span', class_="jdgm-prev-badge__text")
        quote['rating'] = rating_tag.text.strip().replace("reviews", '') if rating_tag else 'Rating not found'

        data.append(quote)

df = pd.DataFrame(data)

# Use both current date and time for a unique filename
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Write the DataFrame to a CSV file with the current date and time in the filename
df.to_csv(f'heritage_jewels_best_sellers_{current_time}.csv', index=False)

print(f"Data written to heritage_jewels_best_sellers_{current_time}.csv")
