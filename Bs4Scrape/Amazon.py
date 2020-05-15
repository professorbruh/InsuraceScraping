from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import csv

url = "https://www.amazon.in/s?k=Face+masks&ref=nb_sb_noss_2"

uClient = uReq(url)

page_html = uClient.read()

uClient.close()

parsed_page = soup(page_html,"html.parser")

containers = parsed_page.find_all("div", {"data-component-type": "s-search-result"})

f = open("products.csv", "w")

write = csv.writer(f,delimiter=',')

write.writerow(["Item", "Price", "Rating"])

for container in containers:

    name = container.find("span", class_="a-size-base-plus a-color-base a-text-normal")

    rating = container.find("a", href="javascript:void(0)", class_="a-popover-trigger a-declarative")

    price = container.find("span", class_="a-price-whole")

    if price is None:

        write.writerow([str(name.text),str(rating.text),"No Price"])
    elif rating is None:

        write.writerow([str(name.text), "No Rating", str(price.text)])

    else:

        write.writerow([str(name.text), str(rating.text), str(price.text)])





