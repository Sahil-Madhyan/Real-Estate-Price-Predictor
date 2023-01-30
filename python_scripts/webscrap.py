from attr import attr, attrs
from bs4 import BeautifulSoup
import pandas
import requests
import os
import numpy as np

bhk = []
prices = []
locations = []
area = []
url = input("Enter the url: ")
pagesEnter = int(input("Enter the number of pages to be scrapped: "))
pages = np.arange(1, pagesEnter, 1)
extension = "?page=" #default extension
x = "&"
if(x in url):
    extension = "&page=" #extension if '&' is present in ur
for page in pages:
    req = requests.get( url+str(extension)+str(page))  # url of makaan.com

    # giving the text to html parser
    soup = BeautifulSoup(req.text, "html.parser")

    # finding the bhk value in 'a' tag named class 'typelink' containing 'span' tag.
    for b in soup.find_all('a', attrs={'class': 'typelink'}):
        bh = b.find('span', attrs={'class': 'val'})
        if(bh == None):
            bhk.append("None")
        else:
            bhk.append(bh.text)

    print(bhk)

    # finding price in 'td' tag named class 'price'
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

    # getting the page number
    for pg in soup.find_all('div', attrs={'class': 'pagination'}):
        pge = pg.find('a', attrs={'aria-label': 'nextPage'}).get('href')

    print(pge)


# assigning all the fetched value to dictionary
data = {"BHK": bhk, "Area": area, "Price": prices, "Location": locations}
# converting the dictionary to frame
frame = pandas.DataFrame.from_dict(data, orient='columns')
# checking if given name.csv is already presented in the given path or not
fileName = input("Enter the filename to be saved: ")
if(os.path.isfile(str(fileName) + str(".csv"))):
    os.remove(str(fileName) + str(".csv"))
# converting frame to csv
frame.to_csv(str(fileName) + str(".csv"), index=True)
