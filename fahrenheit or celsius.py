'''
Author:sidharth.S
date:08-10-2024
TO  CHANGE THE FAHRANHEIT VALUT TO CELSIUS AND VICE-VERSA
'''




temperature=float(input("enter the temperature:"))
unit=input("is the temperature is fahrenheit or celsius(C or f):")
if unit=="C" or unit=="c":
    faran=(9/5*temperature)+32
    print(int(faran),"°F")
elif unit=="F" or unit=="f":
    cels=5/9*(temperature-32)
    print(int(cels),"°C")
else:
    print("!!WRONG UNIT!!")
