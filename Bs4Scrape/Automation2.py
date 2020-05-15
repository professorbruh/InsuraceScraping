from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup as soup
import csv
import os
from selenium.webdriver.chrome.options import Options


z_list = open("testcodes.dat")

file_size = os.stat("results.csv").st_size

f = open("results.csv", "a")

state_code = input("State Code:")

flag = True

write = csv.writer(f,delimiter=',')

if file_size == 0:
    write.writerow(["ZipCode", "Personal Property Coverage", "Deductible", "Liability", "Average Rate", "Highest Rate","Lowest Rate"])
    f.flush()

time.sleep(5)

def writetocsv(current_zipcode,flag):

    for i in range(0, 3):

        ppc.select_by_index(i)

        for j in range(0, 2):

            deductible.select_by_index(j)

            for k in range(0, 2):
                if flag:
                    flag = False
                    cont = open("continuation.csv", "r")

                    if os.stat("continuation.csv").st_size != 0:

                        cont_read = csv.reader(cont)

                        loop_variables=next(cont_read)

                        i = int(str(loop_variables)[11])

                        j = int(str(loop_variables)[16])

                        k = int(str(loop_variables)[21])

                        ppc.select_by_index(i)

                        deductible.select_by_index(j)

                liability.select_by_index(k)

                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="nn"]/button').click()

                html = soup(driver.page_source, "html.parser")

                m = html.find("div", class_="average-rate-container")

                current_ppc = str(
                    html.find("div", class_="form-group personal_property_filter").find("span", class_="opt").text)

                current_deductible = str(html.find("div", class_="form-group deductible").find("span", class_="opt").text)

                current_liability = str(html.find("div", class_="form-group liability").find("span", class_="opt").text)

                avg_rate = str(m.find("span", style="font-weight:bold; color:#003d5b;font-size:45px !important;").text)

                highest_rate=str(html.find("span",class_="highest-rate").find("span", class_="high-low-rate").text)

                lowest_rate=str(html.find("span",class_="pad_left_20").find("span", class_="high-low-rate").text)

                write.writerow([current_zipcode, current_ppc, current_deductible, current_liability, avg_rate, highest_rate,lowest_rate])
                f.flush()

                cont = open("continuation.csv", "w")

                write_cont = csv.writer(cont, delimiter=",")

                write_cont.writerow([current_zipcode, i, j, k,])
                cont.flush()


chrome_options = Options()

chrome_options.add_argument("--headless")

driver=webdriver.Chrome(options=chrome_options, executable_path="F:\Scraping\chromedriver.exe")

driver.get("https://www.insurance.com/home-and-renters-insurance/home-insurance-basics/renters-insurance.html")

time.sleep(5)

zipcode=driver.find_element_by_name("zc")

ppc=Select(driver.find_element_by_name("tool_option"))

deductible=Select(driver.find_element_by_name("deductible"))

liability=Select(driver.find_element_by_name("liability"))

z_reader=csv.reader(z_list,delimiter="\t")

flag2 = True


if os.stat("continuation.csv").st_size == 0:
    flag2 = False
'''
cont_open=open("continuation.csv", "w")
writing_cont=csv.writer(cont_open,delimiter=",")                #Have to work on later
cont_open=open("continuation.csv", "r")             
reading_cont=csv.reader(cont_open,delimiter=",")
'''

for zcode in z_reader:
    if flag:
        current_state = str(zcode)[11:13]
        if current_state != state_code:
            continue

    if str(zcode)[11:13] == state_code:
        zipcode.send_keys(str(zcode)[2:7])
        writetocsv(str(zcode)[2:7], flag)

f.close()

driver.close()
