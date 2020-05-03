from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup as soup
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))

driver.maximize_window()

driver.get("https://www.carinsurance.com/calculators/average-car-insurance-rates.aspx")

time.sleep(3)

slider=driver.find_element_by_xpath("/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/div[2]/label["+str(2)+"]")

for k in range(1,10):
    driver.find_element_by_xpath("/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/div[2]/label["+str((k%2)+1)+"]").click()

for k in range(1,10):
    slider=driver.find_element_by_xpath("/html/body/main/article/section/section/div/div[3]/section[2]/div[3]/form/div[3]/div[2]/div["+str((k%3)+1)+"]"+"/label")
    slider.click()


age = Select(driver.find_element_by_xpath('//*[@id="zip-tool-input-age"]'))

age.select_by_index("18")

m=driver.find_element_by_name("zc")

m.clear()

m.send_keys("95002")

html = soup(driver.page_source, "html.parser")

print(str(html.find("span",class_="zip-monthly-premium-value").text))

print(str(html.find("span",class_="highest-rate-amount px-2").find("span",class_="rate-amount").text))

print(str(html.find("span",class_="lowest-rate-amount px-2").find("span",class_="rate-amount").text))

time.sleep(5)

driver.close()