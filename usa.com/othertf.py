from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

url = "http://www.usa.com/99501-ak-income-and-careers.htm"

uClient = uReq(url)

page_html = uClient.read()

parsed_page = soup(page_html, "html.parser")

uClient.close()

container = parsed_page.find_all("table")
c2= parsed_page.find_all("h3")
container_dict = {}
print(len(c2),",",len(container))

header_dict = {

    0 : "Empty",

    1 : "Per_Capita_Income",

    2 : "Median_Individual_Worker_Income",

    3:  "Median_Individual_Worker_Income",

    4:  "Median_Individual_Worker_Income",

    5:  "Household_Income",

    6:  "Household_Income",

    7:  "Household_Income",

    8:  "Household_Income",

    9:  "Family_Income",

    10:  "Family_Income",

    11: "Median_Household_Income_by_Races",

    12: "Median_Household_Income_by_Age",

    13: "Employment Status",

    14: "Commuting_to_Work",

    15: "Commuting_to_Work",

    16: "Careers",

    17: "Careers",

    18: "Poverty Level"
}
index = -1

for i in container:
    index+=1
    print("This is ",index,"\n")
    j = i.find_all("tr")
    print(len(j))
    for k in j:
        m = k.find_all("td")
        key = m[0].text
        if key.find(":") > 0:
            key = key[0:len(key)-1]
        print(key, m[1].text)


print(len(container))
