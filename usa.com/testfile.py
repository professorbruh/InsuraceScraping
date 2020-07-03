from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

url = "http://www.usa.com/99501-ak-population-and-races.htm"

uClient = uReq(url)

page_html = uClient.read()

parsed_page = soup(page_html, "html.parser")

uClient.close()

container = parsed_page.find_all("table", class_="tbb")

container_dict = {}

for i in container:
    j = i.find_all("tr")
    for k in j:
        m = k.find_all("td")
        key = m[0].text
        if key.find(":") > 0:
            key = key[0:len(key)-1]
        print(key, m[1].text)


print(len(container))