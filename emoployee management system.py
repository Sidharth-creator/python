l=[("john","accounting",50000.0),("jerry","manager",100000),("kevin","CEO",10000000)]
totaanual=0
for i in l:
    if i[-1]>50000:
        print("Employees having salary above 50000:",i[0])
        totaanual=totaanual+i[-1]
print("TOTAL ANNUAL PAYROLL:",totaanual)
