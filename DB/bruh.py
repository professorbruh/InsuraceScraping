import datetime
x = datetime.datetime.now()
date = str(x.strftime("%x")).replace('/','-')
date=date[6:]+'-'+date[3:5]+'-'+date[0:2]
print(date)
