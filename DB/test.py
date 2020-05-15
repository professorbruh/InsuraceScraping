import pyodbc
import pandas as pd
import csv

server = '173.48.206.234'
database = 'M3Q_DATA_BANK'
username = 'WEBSCRAPER'
password = 'webscraper123'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print("Connection to server successful")
f = open("testing.csv", 'w')

writer=csv.writer(f,delimiter=',')

writer.writerow(["ZipCode", "Personal Property Coverage", "Deductible", "Liability", "Average Rate", "Highest Rate", "Lowest Rate"])

cursor=cnxn.cursor()

cursor.execute('SELECT * FROM [dbo].[Renters_Premium_Insurance-com]')
k=0
for row in cursor:
    writer.writerow([row[3], row[4], row[5], row[6], row[7], row[8], row[9]])





