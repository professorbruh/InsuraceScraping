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

index = 0
outer_dict = {}
inner_dict = {}
inter_dict = {}
inter_index = 0

for i in container:

    if index == 0:
        index+=1
        continue

    outer_key = header_dict[index]
    j = i.find_all("tr")
    inner_key = header_dict[index]

    for k in j:
        m = k.find_all("td")
        key = m[0].text
        if inner_key == "\\xa0":
            continue
        if key.find(":") > 0:
            key = key[0:len(key)-1]
        inner_dict [key] = str(m[1].text)

    inter_dict[inter_index] = inner_dict
    inter_index+=1
    #print(inter_dict)

    if index!= 18 and inner_key != header_dict[index+1]:
        print("Current is ",header_dict[index],"\n","Next is :",header_dict[index+1])
        if outer_key == "\xa0":
            continue
        outer_dict [outer_key] = inter_dict
        inner_dict = {}
        inter_dict = {}
        inter_index = 0

    else:
        outer_dict[outer_key] = inter_dict
    index += 1





print(outer_dict)
