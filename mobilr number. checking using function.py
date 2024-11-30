def mobnum():
    num=input("enter the number:")
    totalno=1
    firstno=0
    for i in num:
        totalno=totalno+1
    if totalno==10 and num[0]=="7"or num[0]=="9"or num[0]=="8":
        print("it isa a valid no")
    else:
        print("not a valid no")
mobnum()

