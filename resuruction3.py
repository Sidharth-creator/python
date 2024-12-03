def mult(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mult(n1,n2-1)
f=mult(5,3)
print(f)