from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup as soup
import csv
import os
import sys
import os.path
from selenium.webdriver.chrome.options import Options

#start_time = time.time()

if len(sys.argv) == 1:
    print("This program needs needs an input state")
    exit()
state_code=str(sys.argv[1])

flag=True

f = 0

if os.path.exists(state_code+".csv"):

    f = open((state_code+".csv"),'a')

else:

    f = open((state_code + ".csv"), 'w')

print("Checking CSV files")

write = csv.writer(f,delimiter=',')

dict_i = {"20,000" : 0, "40,000" : 1, "60,000" : 2}

dict_j = {'500' : 0, '1,000' : 1}

dict_k = {'100,000' : 0, '300,000' : 1}
print("Dictionaries initialized")

cont_i = 0
cont_j = 0
cont_k = 0


flag_zip = True

if os.stat(state_code + ".csv").st_size == 0:
    flag_zip = False
    write.writerow(["ZipCode", "Personal Property Coverage", "Deductible", "Liability", "Average Rate", "Highest Rate", "Lowest Rate"])
    f.flush()

    cont_i = 0
    cont_j = 0
    cont_k = 0

else:
    m = open((state_code + ".csv"), "r")

    state_reader = csv.reader(m)

    next(state_reader)

    for reading in state_reader:

        if str(reading) == "[]" and reading is not None:

            continue

        else:

            cont_i = dict_i[str(reading[1])[1:]]

            cont_j = dict_j[str(reading[2])[1:]]

            cont_k = dict_k[str(reading[3])[1:]]

def writetocsv(current_zipcode):
    global cont_j
    global cont_k
    global flag
    for i in range(cont_i, 3):

        ppc.select_by_index(i)

        for j in range(cont_j, 2):

            deductible.select_by_index(j)

            for k in range(cont_k, 2):
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
                if flag:
                    flag = False
                    cont_j = 0
                    cont_k = 0



                print("Writing to csv with indexes i j k =", i, j, k)

                write.writerow([current_zipcode, current_ppc, current_deductible, current_liability, avg_rate, highest_rate,lowest_rate])
                f.flush()


chrome_options = Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path=os.path.abspath("chromedriver.exe"))

print("Initializing driver")

driver.get("https://www.insurance.com/home-and-renters-insurance/home-insurance-basics/renters-insurance.html")

time.sleep(5)

print("Finding required elements")

zipcode=driver.find_element_by_name("zc")

ppc = Select(driver.find_element_by_name("tool_option"))

deductible = Select(driver.find_element_by_name("deductible"))

liability = Select(driver.find_element_by_name("liability"))

print("Opening zipcode.dat...")

z_list=open("zipcode.dat", "r")
flag1=True
z_reader = csv.reader(z_list, delimiter="\t")

last_zipcode = None

reading=0
if flag_zip:

    q = open((state_code + ".csv"), "r")

    q_reader=csv.reader(q)

    for reading in q_reader:
        if reading is not None and str(reading) != "[]" and str(reading[0]) != "ZipCode":
            last_zipcode = str(reading[0])

print(last_zipcode)

flag_zip1 = True

for zcode in z_reader:
    if str(zcode[1]) != state_code:
        continue
    elif str(zcode[0]) != last_zipcode and flag_zip1 and flag_zip:
        continue
    elif str(zcode[0]) == last_zipcode:
        flag_zip1 = False

        zipcode.send_keys(str(zcode[0]))

        writetocsv(str(zcode[0]))
    else:
        print("Zipcode:",str(zcode[0]))

        zipcode.send_keys(str(zcode[0]))

        writetocsv(str(zcode[0]))

    if flag1:
        flag1 = False
        cont_i = 0
        cont_j = 0
        cont_k = 0

    #print("Time taken for ", str(zcode[0]), ":", round(time.time() - start_time)," seconds")

driver.close()




