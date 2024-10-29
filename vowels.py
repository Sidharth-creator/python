
'''
Author:sidharth.S
date:08-10-2024
'''


string=input("enter the string:")
num=0
for i in string:
    if i in "aeiouAEIOU":
        num=num+1
print("number of vowels in word",string,"is:",num)
