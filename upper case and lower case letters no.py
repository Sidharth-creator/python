string=input("enter the string:")
upper=0
lower=0
for i in string:
    if  i.isupper():
        upper=upper+1
    elif i.islower:
        lower=lower+1
print("NO OF UPPER CASE LETTERS:",upper)
print("NO OF LOWER CASE LETTER :",lower)