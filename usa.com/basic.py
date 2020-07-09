from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import json

import csv

import os


def to_json():
    parsed_page = soup(page_html, "html.parser")

    container = parsed_page.find("td", valign="top")

    tables = container.find_all("tr")

    dict_obj = {}
    act_dict_obj = {}
    for i in tables:
        table_container = i.find_all("td")

        if table_container[1].text.find("rank #") == -1:

            if table_container[1].text.find("see") > 0:
                dict_obj[table_container[0].text] = table_container[1].find('a').text

            else:
                dict_obj[table_container[0].text] = table_container[1].text

        else:
            results = table_container[1].find_all('a')
            k = 0
            # print(len(results))
            if len(results) > 1:
                k = 1
            # print(results[k].text)
            inner_dict = {
                table_container[0].text: results[0].text,
                "rank": results[k].text
            }
            dict_obj[table_container[0].text] = inner_dict

    return dict_obj

def to_json2():

    dict_obj = {}

    parsed_page = soup(page_html2,"html.parser")

    container = parsed_page.find_all("table", class_="tbb")

    for i in container:
        j = i.find_all("tr")
        for k in j:
            m = k.find_all("td")
            key = m[0].text
            if key.find(":") > 0:
                key = key[0:len(key) - 1]
            dict_obj[key] = m[1].text
    return dict_obj

def to_json3():

    parsed_page = soup(page_html3, "html.parser")
    container = parsed_page.find_all("table")
    c2 = parsed_page.find_all("h3")
    container_dict = {}

    header_dict = {

        0: "Empty",

        1: "Per_Capita_Income",

        2: "Median_Individual_Worker_Income",

        3: "Median_Individual_Worker_Income",

        4: "Median_Individual_Worker_Income",

        5: "Household_Income",

        6: "Household_Income",

        7: "Household_Income",

        8: "Household_Income",

        9: "Family_Income",

        10: "Family_Income",

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
    inter_index = -1

    for i in container:

        if index == 0:
            index += 1
            continue

        outer_key = header_dict[index]
        j = i.find_all("tr")
        inner_key = header_dict[index]

        for k in j:
            m = k.find_all("td")
            key = m[0].text
            if key.find(":") > 0:
                key = key[0:len(key) - 1]
            inner_dict[key] = str(m[1].text)

        inter_index = inter_index + 1
        inter_dict[inter_index] = inner_dict
        inner_dict = {}

        if index != 18 and inner_key != header_dict[index + 1]:
            # print("Current is ",header_dict[index],"\n","Next is :",header_dict[index+1])
            if outer_key == "\xa0":
                continue
            outer_dict[outer_key] = inter_dict
            inner_dict = {}
            inter_dict = {}
            inter_index = -1

        else:
            outer_dict[outer_key] = inter_dict
        index += 1

    return outer_dict


def to_json4():
    parsed_page = soup(page_html4, "html.parser")

    uClient.close()

    container = parsed_page.find_all("table")

    container_dict = {}

    header_dict = {

        0: "Empty",

        1: "House_Value",

        2: "House_Value",

        3: "Housing_Occupancy",

        4: "Year_Structure_Built",

        5: "Mortage_Status",

        6: "Mortage_Cost",

        7: "Mortage_Cost",

        8: "Mortage_Cost",

        9: "Mortage_Cost",

        10: "No_Mortage",

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
            index += 1
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
                key = key[0:len(key) - 1]
            inner_dict[key] = str(m[1].text)

        inter_index += 1
        inter_dict[inter_index] = inner_dict
        inner_dict = {}

        if index != 19 and inner_key != header_dict[index + 1]:
            # print("Current is ",header_dict[index],"\n","Next is :",header_dict[index+1])
            if outer_key == "\xa0":
                continue
            outer_dict[outer_key] = inter_dict
            inner_dict = {}
            inter_dict = {}
            inter_index = -1

        else:
            outer_dict[outer_key] = inter_dict
        index += 1

    return outer_dict

f = open("zipcode.dat", "r")
page_html = None
reader = csv.reader(f, delimiter="\t")

for i in reader:
    url = "http://www.usa.com/" + i[0] + "-" + i[1].lower() + ".htm"
    url2 = "http://www.usa.com/"+i[0]+"-"+i[1]+"-population-and-races.htm"
    url3 =  "http://www.usa.com/"+i[0]+"-"+i[1].lower()+"-income-and-careers.htm"
    url4 =  "http://www.usa.com/"+i[0]+"-"+i[1].lower()+"-housing.htm"
    print(i[0])

    path = os.getcwd() + "\\" + i[0]

    os.mkdir(path)

    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    uClient2 = uReq(url2)
    page_html2 = uClient2.read()
    uClient2.close()

    uClient3 = uReq(url3)
    page_html3 = uClient3.read()
    uClient3.close()

    uClient4 = uReq(url4)
    page_html4 = uClient4.read()
    uClient4.close()

    basic_info = to_json()
    population = to_json2()
    income_careers = to_json3()
    housing = to_json4()
    print(housing)

    filepath_basic = path + "\\" + "basic_info.html"
    filepath_population = path + "\\" + "population.html"
    filepath_income_careers = path+ "\\" + "income_careers.html"
    filepath_housing = path + "\\" + "housing.html"

    file_basic = open(filepath_basic, 'w')
    file_basic.write(str(page_html))

    file_population = open(filepath_population, "w")
    file_population.write(str(page_html2))

    file_income_careers = open(filepath_income_careers, 'w')
    file_income_careers.write(str(page_html3))

    file_housing = open(filepath_housing,'w')





