import pyodbc
import pandas as pd
import sys
import datetime
import time
start_time = time.time()

if len(sys.argv) == 1:
    print("This program needs needs an input state")
    exit()

state_code = str(sys.argv[1])

f = open(state_code+".csv", "r")

data = pd.read_csv(state_code+".csv")

df = pd.DataFrame(data, columns= ['ZipCode','Personal Property Coverage','Deductible','Liability','Average Rate','Highest Rate','Lowest Rate',"Date","AFlag"])

cols = df.columns

cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, str) else x)

df.columns = cols
x = datetime.datetime.now()
date = x.strftime("%x")

df.loc[:,'Date'] = x
df.loc[:,'AFlag'] = "Y"

server = '173.48.206.234'
database = 'M3Q_DATA_BANK'
username = 'WEBSCRAPER'
password = 'webscraper123'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print("Connection to server successful")


cursor = cnxn.cursor()


insert_query = '''INSERT INTO [dbo].[Renters_Premium_Insurance-com] (Zipcode, Pers_Property_Coverage, Deductible, Liability,Average_Rate,
                Highest_Rate, Lowest_Rate, CREATE_DATE, Active_Flag)
                VALUES(?,?,?,?,?,?,?,?,?)'''
ctr=0


for row in cursor:
    k = (row[3], row[4], row[5], row[6], row[7], row[8], row[9])
csv1= 0
flag=False
zipcode=""
for row in df.itertuples():
    while len(str(row.ZipCode))<5:
        zipcode = "0"+zipcode

    csv1 = (str(zipcode), int(row.Personal_Property_Coverage[1:].replace(',', '')),
            int(row.Deductible[1:].replace(',', '')), int(row.Liability[1:].replace(',', '')),
            int(row.Average_Rate[1:].replace(',', '')), int(row.Highest_Rate[1:].replace(',', '')),
            int(row.Lowest_Rate[1:].replace(',', '')))

    if csv1 == k:
        flag = True
for row in df.itertuples():
'''
    if flag:
        if csv1 != k:
            continue
        else:
            flag = False
            continue
    zipcode = str(row[1])

    while len(str(row.ZipCode)) < 5:
        zipcode = "0" + zipcode

    ppc = row[2][1:]
    ppc = ppc.replace(',', '')

    deductible = row[3][1:]
    deductible = deductible.replace(',', '')

    liability = row[4][1:]
    liability = liability.replace(',', '')

    average_rate = row[5][1:]
    average_rate = average_rate.replace(',', '')

    highest_rate = row[6][1:]
    highest_rate = highest_rate.replace(',', '')

    lowest_rate = row[7][1:]
    lowest_rate = lowest_rate.replace(',', '')

    ctr = ctr + 1

    if ctr % 100 == 0:
        print("Time Elapsed = ", round(time.time() - start_time), " seconds")

    values = (zipcode, ppc, deductible, liability, average_rate, highest_rate, lowest_rate, date, "Y")

    print("Inserting " + zipcode, ppc, deductible, liability, average_rate, highest_rate, lowest_rate, date, "Y")

    cursor.execute(insert_query, values)

    cnxn.commit()
'''