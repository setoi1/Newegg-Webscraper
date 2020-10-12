from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/Water-Liquid-Cooling/SubCategory/ID-575?Tid=8008'

userClient = urlopen(url)

rawHTML = userClient.read()

userClient.close()

rawHTMLSoup = BeautifulSoup(rawHTML, 'html.parser')

itemContainers = rawHTMLSoup.findAll('div', {'class':'item-container'})

container = itemContainers[0]

filename = 'ScrapedCoolers.csv'

f = open(filename, 'w')

header = 'Brand, Product Name, Fan Count, Price, Shipping\n'

f.write(header)

for container in itemContainers:

    brand = container.div.div.a.img['title']

    productContainer = container.findAll('a', {'class':'item-title'})
    productName = productContainer[0].text

    fanContainer = container.findAll('a', {'class':'item-title'})
    fanCount = fanContainer[0].text

    if '240' in fanCount:
        numOfFans = '2'
    elif '360' in fanCount:
        numOfFans = '3'

    priceContainer = container.findAll('li', {'class':'price-current'})
    price = priceContainer[0].text

    shippingContainer = container.findAll('li', {'class':'price-ship'})
    shipping = shippingContainer[0].text.strip()

    print('Brand: ' + brand)
    print('Product Name: ' + productName)
    print('Fan Count: ' + numOfFans)
    print('Price: ' + price)
    print('Shipping: ' + shipping)

    f.write(brand + ', ' + productName.replace(',', '|') + ', ' + numOfFans + ', ' + price + ', ' + shipping + ', ' + "\n")

f.close()
