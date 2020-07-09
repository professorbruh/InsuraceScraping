from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

url = "http://www.usa.com/99501-ak-housing.htm"

uClient = uReq(url)

page_html = uClient.read()

parsed_page = soup(page_html, "html.parser")

uClient.close()


container = parsed_page.find_all("table")

container_dict = {}

header_dict = {

    0 : "Empty",

    1 : "House_Value",

    2 : "House_Value",

    3:  "Housing_Occupancy",

    4:  "Year_Structure_Built",

    5:  "Mortage_Status",

    6:  "Mortage_Cost",

    7:  "Mortage_Cost",

    8:  "Mortage_Cost",

    9:  "Mortage_Cost",

    10:  "No_Mortage",

    11: "No_Mortage",

    12: "No_Mortage",

    13: "No_Mortage",

    14: "Units_In_Structure",

    15: "Rooms",

    16: "Bedrooms",

    17: "House_Heating_Fuel",

    18: "Gross_Rent",

    19: "Vehicle_Available"
}

index = 0

outer_dict = {}
inner_dict = {}
inter_dict = {}
inter_index = -1


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
        inner_dict[key] = str(m[1].text)

    inter_index += 1
    inter_dict[inter_index] = inner_dict
    inner_dict = {}

    if index!= 19 and inner_key != header_dict[index+1]:
        #print("Current is ",header_dict[index],"\n","Next is :",header_dict[index+1])
        if outer_key == "\xa0":
            continue
        outer_dict [outer_key] = inter_dict
        inner_dict = {}
        inter_dict = {}
        inter_index = -1

    else:
        outer_dict[outer_key] = inter_dict
    index += 1





print(outer_dict)
