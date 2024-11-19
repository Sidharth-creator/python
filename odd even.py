l1=[]
l2=[]
lim1=int(input("enter the lim in list1:"))
for i in range(lim1):
    user=int(input("enter the number:"))
    l1.append(user)
lim2=int(input("enter the lim in list2"))
for i in range(lim2):
    user2=int(input("enter the number:"))
    l2.append(user2)
print(l1)
print(l2)
l3=l1+l2
print(l3)
evenlst=[]
oddlst=[]
for i in l3:
    if i%2==0:
        evenlst.append(i)
    else:
        oddlst.append(i)
print("EVEN LIST:",evenlst)
print("ODD LIST:",oddlst)
evenlst.sort()
oddlst.sort()
com=oddlst+evenlst
print(com)



