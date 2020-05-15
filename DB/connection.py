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
date = x.strftime("%x")

insert_query = '''INSERT INTO [dbo].[Renters_Premium_Insurance-com] (Zipcode, Pers_Property_Coverage, Deductible, Liability,Average_Rate,
                Highest_Rate, Lowest_Rate, CREATE_DATE, Active_Flag)
                VALUES(?,?,?,?,?,?,?,?,?)'''
ctr=0

k=0
cursor.arraysize = 1000

flag = False
for row in reader:
    zipcode = row[0]

    if len(zipcode) == 4:
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

    ctr=ctr+1

    if ctr % 100 == 0:
        print("Time Elapsed = ", round(time.time() - start_time)," seconds")

    values = (zipcode, ppc, deductible, liability, average_rate, highest_rate, lowest_rate, date, "Y")

    print("Inserting "+zipcode ,ppc , deductible, liability, average_rate, highest_rate, lowest_rate,date, "Y")

    cursor.execute(insert_query, values)
    if ctr % 1000 == 0:
        cnxn.commit()

cnxn.commit()


