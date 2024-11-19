lst=[]

stockno=int(input("enter the stock:"))
for i in range(stockno):
    stockname=input("enter the name of stock:")
    stockqty=int(input("enter the quantity of stock:"))
    stockprice=float(input("enter the price of stock:"))
    tup=(stockname,stockqty,stockprice)
    lst.append(tup)
print(lst)
hstockval=0
itmval=""
for i in lst:
    itemname,itemqty,itemprice=i
    print("itemname","\titemqty","\titemprice","\ttotal value of stock")
    total_value = itemqty * itemprice
    if hstockval<total_value:
        hstockval=total_value
        itmval=itemname
        print(itemname,2*"\t",itemqty,2*"\t",itemprice,2*"\t",total_value)
print("item with highest stock value:",hstockval,"is",itmval)
