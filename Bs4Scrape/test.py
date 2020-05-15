from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

import requests
from datetime import datetime
import sys
import importlib
import pdb
#Column Heading - Things to do,	Zip code,	Phone no,	Address Line 1,	Address Line 2,	Address Line 3


h_list = open('zipcode.dat')
h_reader = csv.reader(h_list, delimiter='\t')

url = 'https://www.yelp.com/search?{}={}&find_loc={}'

csv.register_dialect('myDialect1',
                     quoting=csv.QUOTE_ALL,
                     skipinitialspace=True)

f = open('things+to+do-' + inputState +  '.csv', 'w')
writer = csv.writer(f, dialect='myDialect1')
writer.writerow(['Things to do', 'Zip Code', 'Phone', 'Address Line1', 'Address line2'])

for zcode in h_reader:
    #print(zcode)
    stateCode = zcode[1]
    if (inputState == stateCode):
        print('inside if')
        urlZip = zcode[0]
        print(url.format('find_desc', 'things+to+do', urlZip))
        my_url = url.format('find_desc', 'things+to+do', urlZip)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("li", {
            "class": "lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU"})
        zipCode = ''
        things_to_do = ''
        count = 0
        for container in containers:
            # print(soup.prettify(container))
            if container.find('h4', class_='lemon--h4__373c0__1yd__ heading--h4__373c0__27bDo alternate__373c0__2Mge5'):
                if '.' in container.find('h4', class_='lemon--h4__373c0__1yd__ heading--h4__373c0__27bDo alternate__373c0__2Mge5').text.split(' ')[0]:
                    count = count + 1
                    things_to_do = container.find('h4', class_='lemon--h4__373c0__1yd__ heading--h4__373c0__27bDo alternate__373c0__2Mge5').find('a').attrs['name']
                    if len(container.findAll('div', class_='lemon--div__373c0__1mboc secondaryAttributes__373c0__7bA0w arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU')) > 0:
                        PhoneAddressDiv = container.find('div', class_='lemon--div__373c0__1mboc container__373c0__19wDx padding-l2__373c0__1Dr82 border-color--default__373c0__3-ifU text-align--right__373c0__1XDu3')
                        phone = ''
                        addressLine1 = ''
                        addressLine2 = ''
                        for subDiv in PhoneAddressDiv.children:
                            #print('subDiv',subDiv)
                            if subDiv != None:
                                tagName = subDiv.name
                                if(tagName == 'div'):
                                    if subDiv.findAll('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO'):
                                        PhAddContainer = subDiv.find('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO').find('span')
                                        if PhAddContainer != None:
                                            addressLine2Container = subDiv.find('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO').find('span')
                                            if addressLine2Container != None :
                                                addressLine2 = addressLine2Container.text
                                            else:
                                                addressLine2 = '#'
                                        else:
                                            phoneContainer = subDiv.find('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO')
                                            if phoneContainer != None:
                                                phone = phoneContainer.text
                                            else:
                                                phone = '#'
                                elif (tagName == 'address'):
                                        addressLine1Container = subDiv.findAll('span', class_='lemon--span__373c0__3997G raw__373c0__3rcx7')[0]
                                        if addressLine1Container != None:
                                            addressLine1 = addressLine1Container.text
                                        else:
                                            addressLine1 = '#'

                    if len(container.findAll('div',class_='lemon--div__373c0__1mboc priceCategory__373c0__3zW0R display--inline-block__373c0__1ZKqC border-color--default__373c0__3-ifU')) > 0:
                        if container.find('div', class_='lemon--div__373c0__1mboc priceCategory__373c0__3zW0R display--inline-block__373c0__1ZKqC border-color--default__373c0__3-ifU').find('a').attrs['href']:
                            zipContainer = container.find('div', class_='lemon--div__373c0__1mboc priceCategory__373c0__3zW0R display--inline-block__373c0__1ZKqC border-color--default__373c0__3-ifU').find('a').attrs['href']
                            zipCode = '\''+ zipContainer.split('find_loc=')[len(zipContainer.split('find_loc=')) - 1] + '\''
                        else:
                            zipCode = '#'
                    else:
                        zipCode = '#'
                    writer.writerow([things_to_do, zipCode, phone, addressLine1, addressLine2])
                    exit(1)
                    f.flush()
                    print(things_to_do, zipCode, phone, addressLine1, addressLine2)
f.close()

