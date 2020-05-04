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

write = csv.writer(f, delimiter=',')

dict_i = {"30" : 10, "50" : 14, "70" : 18}

rev_i = {10: "30", 14: "50", 18: "70"}

dict_j = {'Male' : 0, 'Female' : 1}

rev_j = {0 : 'Male', 1 : 'Female'}

dict_k = {'State Minimum Liability': 0, 'Liability Only - $50K/$100/$50K': 1, 'Full Coverage - $100K/$300K/$100K': 2}

rev_k = {0 : 'State Minimum Liability', 1 : 'Liability Only - $50K/$100/$50K', 2: 'Full Coverage - $100K/$300K/$100K'}

print("Dictionaries initialized")

cont_i = 10
cont_j = 0
cont_k = 0


flag_zip = True

if os.stat(state_code + ".csv").st_size == 0:
    flag_zip = False
    write.writerow(["ZipCode", "Age", "Gender", "Coverage Type", "Average Monthly Premium", "Highest Rate", "Lowest Rate"])
    f.flush()

    cont_i = 10
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

            cont_i = dict_i[str(reading[1])]

            cont_j = dict_j[str(reading[2])]

            cont_k = dict_k[str(reading[3])]

def writetocsv(current_zipcode):
    global cont_j
    global cont_k
    global flag
    for i in range(cont_i, 19,4):

        age.select_by_index(i)

        for j in range(cont_j, 2):

            time.sleep(5)

            driver.find_element_by_xpath("/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/div[2]/label["+str(j+1)+"]").click()

            for k in range(cont_k, 3):

                driver.find_element_by_xpath("/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/div[3]/div[2]/div["+str(k+1)+"]"+"/label").click()
                time.sleep(2)

                driver.find_element_by_xpath('/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/input[2]').click()

                time.sleep(3)

                html = soup(driver.page_source, "html.parser")

                average_monthly_premium = str(html.find("span", class_="zip-monthly-premium-value").text)

                highest_rate = str(html.find("span",class_="highest-rate-amount px-2").find("span",class_="rate-amount").text)

                lowest_rate = str(html.find("span",class_="lowest-rate-amount px-2").find("span",class_="rate-amount").text)
                if flag:
                    flag = False
                    cont_j = 0
                    cont_k = 0
                print("Writing to csv with indexes i j k =", i, j, k)

                write.writerow([current_zipcode, rev_i[i], rev_j[j], rev_k[k], average_monthly_premium, highest_rate,lowest_rate])
                f.flush()
chrome_options = Options()

chrome_options.add_argument("--headless")

chrome_options.add_argument('window-size=1920x1080');

driver = webdriver.Chrome(options=chrome_options, executable_path=os.path.abspath("chromedriver.exe"))

print("Initializing driver")

driver.get("https://www.carinsurance.com/calculators/average-car-insurance-rates.aspx")

driver.maximize_window()

time.sleep(5)

print("Finding required elements")

zipcode = driver.find_element_by_name("zc")

age = Select(driver.find_element_by_xpath('//*[@id="zip-tool-input-age"]'))

coverage_type = driver.find_element_by_xpath("/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/div[3]/div[2]/div["+str(1)+"]"+"/label")

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

        zipcode.clear()

        zipcode.send_keys(str(zcode[0]))

        writetocsv(str(zcode[0]))
    else:
        print("Zipcode:",str(zcode[0]))

        zipcode.clear()

        zipcode.send_keys(str(zcode[0]))

        writetocsv(str(zcode[0]))

    if flag1:
        flag1 = False
        cont_i = 10
        cont_j = 0
        cont_k = 0

    #print("Time taken for ", str(zcode[0]), ":", round(time.time() - start_time)," seconds")

driver.close()




