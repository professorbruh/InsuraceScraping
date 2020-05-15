from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.flipkart.com/search?q=Masks&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(url)

page_html = uClient.read()

uClient.close()

parsed_page = soup(page_html , "html.parser")

container_product=parsed_page.find_all("a" , class_ = "_2cLu-l")

container_rating=parsed_page.find_all("div" , class_ = "hGSR34")

container_price=parsed_page.find_all("div" , class_="_1vC4OE")

for i in range(0,len(container_product)):
    print("Product "+ str(i+1))
    print(container_product[i].text)
    print(container_rating[i].text)
    print(container_price[i].text)