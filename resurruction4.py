def gcd(n1,n2):
    if n1%n2==0:
        return n1
    else:
        gcd(n1,n1%n2)
f=gcd(5,2)
print(f)