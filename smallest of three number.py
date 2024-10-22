'''
Author:sidharth.S
date:08-10-2024
TO FIND THE SMALLEST NUMBER FROM THREE
'''




number1=int(input("enter the number 1:"))
number2=int(input("enter the number 2:"))
number3=int(input("enter the number3:"))
if number1<number2 and number1<number3:
    print(number1,"is the smallest")
elif number2<number1 and number2<number3:
    print(number2,"is the smallest")
elif number3<number1 and number3<number2:
    print(number3,"is the smallest")
else:
    print("they are equal")
