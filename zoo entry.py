age=int(input("enter the age"))
if age<10:
    print("ticket price=7")
elif age>10 or age==10 and age<60:
    print("ticket price=10")
elif age>60 or age==60:
    print("ticket rate=5")
else:
    print("NO ENTRY")