from datetime import datetime
currenttime=datetime.now()
print(currenttime)
datte=currenttime.strftime("%m-%d-%y")
print("date:",datte)
datetime=currenttime.strftime("%Y-%m-%d %H:%M:%S")
print(datetime)
year=currenttime.strftime("%Y-%m-%d")
time=currenttime.strftime("%H:%M:%s %p")
data=currenttime.strftime("%a-%m-%d %H:%M:%s IST %Y")
a=currenttime.strftime("%m")
b=currenttime.strftime("%Y")
c=currenttime.strftime("%Y-%m-%d, %H:%M:%S,%f%z")
print(year)
print(time)
print(data)
print(a)
print(b)
print(c)