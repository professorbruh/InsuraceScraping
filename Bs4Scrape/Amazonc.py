from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import csv

url = "https://www.amazon.in/s?k=Coffee&ref=nb_sb_noss"

uClient = uReq(url)

page_html = uClient.read()

uClient.close()

parsed_page = soup(page_html,"html.parser")

container_product=parsed_page.find_all("div", class_="a-section aok-relative s-image-square-aspect")

container_rating=parsed_page.find_all("a", href="javascript:void(0)", class_="a-popover-trigger a-declarative")

container_price=parsed_page.find_all("span", class_="a-price")

print(container_price[0].text)

