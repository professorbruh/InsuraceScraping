from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.dota2.com/patches/"

uClient = uReq(url)

page_html = uClient.read()

uClient.close()

parsed_page = soup(page_html , "html.parser")

k=str(parsed_page.prettify())

f=open("htmlcode.csv" , "w")

f.write(k)

f.close()

container_general=parsed_page.find_all("div" , id= "GeneralSection")

container_items=parsed_page.find_all("div" , id="ItemsSection")

container_heroes=parsed_page.find_all("div" , id="HeroesSection")

for general in container_general:
    print(general.text)

for items in container_items:
    print(items.text)

for heroes in container_heroes:
    print(heroes.text)