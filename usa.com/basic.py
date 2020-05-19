from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import json

import csv

import os


def to_json(zip):
    parsed_page = soup(page_html, "html.parser")

    container = parsed_page.find("td", valign="top")

    tables = container.find_all("tr")

    dict_obj = {}
    dict_obj["Zipcode"] = zip

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

    with open('test.json', 'a') as json_file:
        json.dump(dict_obj, json_file,indent = 4, separators="\t\n")

f = open("zipcode.dat", "r")
page_html = None
reader = csv.reader(f, delimiter="\t")

for i in reader:
    url = "http://www.usa.com/" + i[0] + "-" + i[1].lower() + ".htm"
    print(url)
    uClient = uReq(url)

    page_html = uClient.read()

    uClient.close()
    to_json(i[0])
