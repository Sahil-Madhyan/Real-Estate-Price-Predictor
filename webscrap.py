from attr import attr, attrs
from bs4 import BeautifulSoup
import pandas
import requests
import os
import numpy as np

pages = np.arange(1,2,1)
bhk = []
prices = []
locations = []
area = []
for page in pages:
    req = requests.get(
        "https://www.makaan.com/bangalore-residential-property/buy-property-in-bangalore-city?page="+str(page))

    soup = BeautifulSoup(req.text, "html.parser")

    

    for b in soup.find_all('a', attrs={'class': 'typelink'}):
        bh = b.find('span', attrs={'class': 'val'})
        if(bh == None):
            bhk.append("None")
        else:
            bhk.append(bh.text)

    print(bhk)

    
    for p in soup.find_all('td', attrs={'class': 'price'}):
        pr = p.find('span', attrs={'class': 'val'})
        un = p.find('span', attrs={'class': 'unit'})
        prices.append(pr.text + un.text)

    print(prices)

    
    for l in soup.find_all('span', attrs={'class': 'locName'}):
        la = l.find('span', attrs={'itemprop': 'addressLocality'})
        lc = l.find('span', attrs={'class': 'cityName'})
        locations.append(la.text + "," + lc.text)

    print(locations)

   
    for a in soup.find_all('td', attrs={'class': 'size'}):
        ar = a.find('span', attrs={'class': 'val'})
        area.append(ar.text)
    
    print(area)

    for pg in soup.find_all('div', attrs={'class': 'pagination'}):
        pge = pg.find('a', attrs={'aria-label': 'nextPage'}).get('href')

    print(pge)


data = {"BHK": bhk, "Area": area, "Price": prices, "Location": locations}
frame = pandas.DataFrame.from_dict(data, orient='columns')
if(os.path.isfile('Bangalore.csv')):
    os.remove('Bangalore.csv')
frame.to_csv('Bangalore.csv', index=True)
