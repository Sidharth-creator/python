def sum(n1,n2):
    if n2==0:
        return n1
    else:
        return sum(n1+1,n2-1)

f=sum(5,3)
print(f)


