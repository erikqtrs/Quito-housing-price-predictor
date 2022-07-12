from bs4 import BeautifulSoup
import pandas as pd
import cloudscraper
import time
scraper = cloudscraper.create_scraper(delay=10)
price_list = []
feature_list = []
location_list = []
for page in range(1,129):
    url = f'https://www.plusvalia.com/casas-en-venta-en-quito-hasta-20-anos-pagina-{page}.html'
    info = scraper.get(url).text
    soup = BeautifulSoup(info, 'lxml')
    prices = soup.find_all('div', attrs={ 'data-qa':'POSTING_CARD_PRICE'  })
    features = soup.find_all('div', attrs = {'data-qa':"POSTING_CARD_FEATURES"})
    locations = soup.find_all('div', attrs={ 'data-qa':'POSTING_CARD_LOCATION' })
    for price in prices:
        price_list.append(price.get_text())
    for feature in features:
        feature_list.append(feature.get_text())
    for location in locations:
        location_list.append(location.get_text())
    time.sleep(0.02)


df = pd.DataFrame({'features': feature_list, 'location': location_list, 'price': price_list})

df.to_csv('houses.csv', index=False)