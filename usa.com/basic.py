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

    dict_obj = {}

    parsed_page = soup(page_html3,"html.parser")

    container = parsed_page.find_all("table")


    

f = open("zipcode.dat", "r")
page_html = None
reader = csv.reader(f, delimiter="\t")

for i in reader:
    url = "http://www.usa.com/" + i[0] + "-" + i[1].lower() + ".htm"
    url2 = "http://www.usa.com/"+i[0]+"-"+i[1]+"-population-and-races.htm"
    url3 =  "http://www.usa.com/"+i[0]+"-"+i[1]+"income-and-careers.htm"
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

    basic_info = to_json()
    population = to_json2()

    filepath_basic = path + "\\" + "basic_info.html"
    filepath_population = path + "\\" + "population.html"

    file_basic = open(filepath_basic, 'w')
    file_basic.write(str(page_html))

    file_population = open(filepath_population, "w")
    file_population.write(str(page_html2))




