from urllib.request import urlopen
from bs4 import BeautifulSoup

# Note: Creating many variables for function/method calls creates cleaner code

# URL to scrape
# url = 'https://www.newegg.com/Water-Liquid-Cooling/SubCategory/ID-575?Tid=8008&PageSize=96'

url = 'https://www.newegg.com/p/pl?N=100008008%20600036012&PageSize=96'

# Calling urlopen onto the url to open a connection using urlopen()
userClient = urlopen(url)

# Reads the raw HTML file using .read()
rawHTML = userClient.read()

# Closes the client to terminate connection using .close()
userClient.close()

# Parses rawHTML by calling BeautifulSoup() onto rawHTML
rawHTMLSoup = BeautifulSoup(rawHTML, 'html.parser')

# Finds all div.class with name "item-container"
itemContainers = rawHTMLSoup.findAll('div', {'class':'item-container'})

container = itemContainers[0]

filename = 'ScrapedCoolers.csv'

f = open(filename, 'w')

header = 'Brand, Product Name, Radiator Size, Price, Shipping\n'

f.write(header)

for container in itemContainers:

    brandName = container.div.div.a.img['title']

    if 'RAIJINTEK CO., LTD' in brandName:
        brandName = 'RAIJINTEK'

    productContainer = container.findAll('a', {'class':'item-title'})
    productName = productContainer[0].text

    fanContainer = container.findAll('a', {'class':'item-title'})
    radiatorSize = fanContainer[0].text

    if '240' in radiatorSize:
        radiatorSizeConversion = '240'
    elif '360' in radiatorSize:
        radiatorSizeConversion = '360'

    priceContainer = container.findAll('li', {'class':'price-current'})
    price = priceContainer[0].text

    shippingContainer = container.findAll('li', {'class':'price-ship'})
    shipping = shippingContainer[0].text.strip()
    
    print('Brand: ' + brandName)
    print('Product Name: ' + productName)
    print('Radiator Size: ' + radiatorSizeConversion)
    print('Price: ' + price)
    print('Shipping: ' + shipping)

    # Writes the values into an excel sheet
    f.write(brandName + ', ' + productName.replace(',', '|') + ', ' + radiatorSizeConversion + ', ' + price + ', ' + shipping + ', ' + "\n")

f.close()