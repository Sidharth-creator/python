check=int(input("enter the no:"))
if check==1 or check==2 or check==3:
    for j in range (1,check+2):
        if check%j==0:
            print(check,"is not prime")
            break
        else:
            print(check,"is prime")
            break
else:
    for i in range(2,(check//2)+1):
        print(i)
        if check%i==0:
            print(check,"is not a prime number")
            break
        else:
            print(check,"prime number")
            break


