import os
import csv
from urllib.request import urlopen as uReq
f = open("zipcode.dat", "r")
page_html = None
reader = csv.reader(f, delimiter="\t")

for i in reader:
    url = "http://www.usa.com/" + i[0] + "-" + i[1].lower() + ".htm"
    url2 = "http://www.usa.com/"+i[0]+"-"+i[1]+"-population-and-races.htm"
    print(i[0])

    path = os.getcwd()+"\\"+i[0]
    os.mkdir(path)
    uClient = uReq(url)

    page_html = uClient.read()

    uClient.close()

    uClient2 = uReq(url2)

    page_html2 = uClient2.read()

    uClient2.close()
    filepath_basic =path+"\\"+"basic_info.html"
    filepath_population = path+"\\"+"population.html"
    file_basic = open(filepath_basic,'w')
    file_basic.write(str(page_html))
    file_population = open(filepath_population,"w")
    file_population.write(str(page_html2))




