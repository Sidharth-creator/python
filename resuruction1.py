def factorial(n1):
    if n1==0:
        return 1
    else:
         return n1*factorial(n1-1)
f=factorial(5)
print(f)