import pyodbc
import csv
import sys
import datetime
import time
start_time = time.time()

if len(sys.argv) == 1:
    print("This program needs needs an input state")
    exit()

state_code = str(sys.argv[1])

f = open(state_code+".csv", "r")

reader = csv.reader(f, delimiter=',')

server = '173.48.206.234'
database = 'M3Q_DATA_BANK'
username = 'WEBSCRAPER'
password = 'webscraper123'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print("Connection to server successful")

x = datetime.datetime.now()
cursor = cnxn.cursor()
next(reader)
date = '2020-14-05'

insert_query = '''INSERT INTO [dbo].[Renters_Premium_Insurance-com] (Zipcode, Pers_Property_Coverage, Deductible, Liability,Average_Rate,
                Highest_Rate, Lowest_Rate, Active_Flag)
                VALUES(?,?,?,?,?,?,?,?)'''
ctr=0

k=0
flag = False
param = []
for row in reader:
    zipcode = row[0]

    while len(zipcode)<5:
        zipcode = "0" + zipcode

    ppc=row[1][1:]
    ppc=ppc.replace(',', '')

    deductible = row[2][1:]
    deductible = deductible.replace(',', '')

    liability = row[3][1:]
    liability = liability.replace(',', '')

    average_rate = row[4][1:]
    average_rate = average_rate.replace(',', '')

    highest_rate = row[5][1:]
    highest_rate = highest_rate.replace(',', '')

    lowest_rate=row[6][1:]
    lowest_rate = lowest_rate.replace(',', '')
    param.append([zipcode, ppc, deductible, liability, average_rate, highest_rate, lowest_rate, "Y"])

cursor.fast_executemany = True
cursor.executemany(insert_query, param)
cnxn.commit()


