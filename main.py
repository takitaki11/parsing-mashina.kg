
import csv

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


URL = 'https://www.mashina.kg/'

response = requests.get(URL)

html = response.text


soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_ = 'category-block-content-item')

result = []

for tag in cards:
    item = tag.a

    title = item.find('div', class_ = 'main-title').text
    price = item.find('div', class_ = 'modal-main-price').text
    img_link = item.find('div', class_ = 'main-image-item visible').find('img').get('src')
    description = item.find('div', class_ = 'seller-comments').text

    print(title)

    obj = {
        'title': title.strip(),
        'price': price.strip(),
        'img_link': img_link.strip(),
        'description': description.strip()
    }

    result.append(obj)


with open('cars.csv', 'w') as file:
    names = ['title', 'price', 'img_link', 'description']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    for car in result:

        writer.writerow(car)