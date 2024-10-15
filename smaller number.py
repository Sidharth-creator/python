
'''author:Sidharth.S
  Date:15-10-2024
  this program is to find the positive number and negative number'''




number1=int(input("enter the first nuber:"))
number2=int(input("enter the second number:"))
number3=int(input("enter ten third number:"))
if number1<number2 and number1<number3:
    print(number1,"is the smallest")
elif number2<number1 and number2<number3:
    print(number2,"is the smallest")
elif number3<number1 and number3<number2:
    print(number3,"is the smallest")
else:
    print("they are equal")
