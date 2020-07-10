from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

url = "http://www.usa.com/99509-ak-school-district.htm"

uClient = uReq(url)

page_html = uClient.read()

uClient.close()

parsed_page = soup(page_html, "html.parser")

school_container1 = parsed_page.find_all("div",class_ = "plb")

school_container2 = parsed_page.find_all("div",class_ = "plw")

index = -1

dict = {}

for i in school_container1:
    index+=1
    dict [index] = i.text

for i in school_container2:
    index+=1
    dict [index] = i.text
