def triangle(base,height,hipot):
    if hipot**2 == base**2+height**2:
        print("it is a right angle triangle")
    else:
        print("not a right angle triangle")
base=int(input("enter the base length:"))
height=int(input("enter the length height:"))
hipot=int(input("enter the the hipotneus length"))
triangle(base,height,hipot)

