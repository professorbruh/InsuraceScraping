import csv
import pandas
z_list = open("testcodes.dat")
z_reader=csv.reader(z_list,delimiter="\t")
for zcode in z_reader:
    print(str(zcode)[2:7])