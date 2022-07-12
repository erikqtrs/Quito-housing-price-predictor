from bs4 import BeautifulSoup
import pandas as pd
import cloudscraper
import time
scraper = cloudscraper.create_scraper(delay=10)

def get_houses(num_pages):
    price_list = []
    feature_list = []
    location_list = []
    # for loop para recorrer cada una de las paginas indicadas
    for page in range(1, num_pages+1):
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
    # transformar los datos recolectados a un dataframe
    df = pd.DataFrame({'features': feature_list, 'location': location_list, 'price': price_list})
    # exportacion de la data a archivo .csv
    df.to_csv('houses.csv', index=False)

num_pages = int( input('Enter number of pages: ') )
get_houses(num_pages)