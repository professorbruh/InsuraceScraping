from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

import json

import csv

import os

f = open("zipcode.dat", "r")
page_html = "http://www.usa.com/99501-ak.htm"
reader = csv.reader(f, delimiter="\t")

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