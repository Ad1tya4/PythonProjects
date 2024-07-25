from bs4 import BeautifulSoup
import requests
# import os
# print(os.getcwd())
str = "https://www.zillow.com"
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfkXFSfzPzVhx0Jkl1C8ifPwnTUHxKd8Do3uFN3GVgaZkp6uw/viewform?usp=sf_link"
zillow = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

from urllib.request import Request, urlopen
from seleniumhandler import Formhandler

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(zillow,headers=hdr)
page = urlopen(req)
html = page.read()
page.close()
soup = BeautifulSoup(html, "html.parser")

# requested_url = checkURL(requested_url)
# try:
#     # define headers to be provided for request authentication
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
#                              'AppleWebKit/537.11 (KHTML, like Gecko) '
#                              'Chrome/23.0.1271.64 Safari/537.11',
#                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#                'Accept-Encoding': 'none',
#                'Accept-Language': 'en-US,en;q=0.8',
#                'Connection': 'keep-alive'}
#     request_obj = Request(url=requested_url, headers=headers)
#     opened_url = urlopen(request_obj)
#     page_html = opened_url.read()
#     opened_url.close()
#     page_soup = soup(page_html, "html.parser")
#     return page_soup, requested_url
#
# except Exception as e:
#     print(e)

# responce = requests.get(zillow)
# responce.raise_for_status()
# website = responce.text
# soup = BeautifulSoup(website,'html.parser')
ul = "List-c11n-8-84-3__sc-1smrmqp-0.StyledSearchListWrapper-srp__sc-1ieen0c-0.doa-doM.fgiidE.photo-cards"
li = ".ListItem-c11n-8-84-3__sc-10e22w8-0.StyledListCardWrapper-srp__sc-wtsrtn-0.iCyebE.gTOWtl script"
list_of_properties = soup.select(li)


list = []
urls = []
addresses = []
ppms = []
for i in list_of_properties:
    value = i.text
    list.append(value)
# print(list[1].split('"')[11])
# print(list[4].split('"')[-10])
# print(list[4].split('"')[-14])
# print(list[1].split('"'))
# print(list[4].split('"'))
print(list[4])
print(list[1])
all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)
print(all_price_elements)
# for i in list:
#     if i.split('"')[3] == "Event":
#         x = i.split('"')[-14]
#         y = i.split('"')[-10]
#         z = f"{x}, CA {y}"
#         addresses.append(z)
#     else:
#         addresses.append(i.split('"')[11])

#     urls.append(value["url"])
# print(urls)

# for i in list:
#     x = i.split('"')[-2]
#     if x == "CA":
#         y= list[4].split('"')[15]
#         x = f"{str}{y}"
#     urls.append(x)
formhandler = Formhandler(form_url)
formhandler.do_stuff()

