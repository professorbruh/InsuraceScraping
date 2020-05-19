from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import json

url = "http://www.usa.com/02111-ma.htm"

uClient = uReq(url)

page_html=uClient.read()

uClient.close()

parsed_page = soup(page_html, "html.parser")

container = parsed_page.find("td",valign ="top")

tables = container.find_all("tr")

dict_obj = {}

for i in tables:
    table_container = i.find_all("td")

    if table_container[1].text.find("rank #") == -1:
        dict_obj[table_container[0].text] = table_container[1].text

    elif table_container[1].text.find("see\x") > 0:
        dict_obj[table_container[0].text] = table_container[1].text

    else:
        print("yes")


print(dict_obj)









