import pandas as pd
import datetime
data = pd.read_csv ('CA.csv')
df = pd.DataFrame(data, columns= ['ZipCode','Personal Property Coverage','Deductible','Liability','Average Rate','Highest Rate','Lowest Rate',"Date","AFlag"])
x = datetime.datetime.now()
date = x.strftime("%x")
df.loc[:,'Date'] = x
df.loc[:,'AFlag'] = "Y"
cols = df.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, str) else x)
df.columns = cols

for row in df.itertuples():
    f = row
    k = (str(row.ZipCode), int(row.Personal_Property_Coverage[1:].replace(',', '')), int(row.Deductible[1:].replace(',', '')), int(row.Liability[1:].replace(',', '')), int(row.Average_Rate[1:].replace(',', '')), int(row.Highest_Rate[1:].replace(',', '')), int(row.Lowest_Rate[1:].replace(',', '')))
print(k)
print(row)