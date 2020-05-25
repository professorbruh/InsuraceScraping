from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

url = "http://www.usa.com/99501-ak-population-and-races.htm"

uClient = uReq(url)

page_html = uClient.read()

parsed_page = soup(page_html, "html.parser")

uClient.close()

container = parsed_page.find_all("table", class_="tbb")

for i in container:
    j = i.find_all("tr")
    for k in j:
        m = k.find_all("td")
        print(m[0].text)
    break


print(len(container))