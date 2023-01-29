#WAP to calculate selling price of book based on cost price and discount.
cp=float(input("Enter cost price of book: "))
discount=int(input("How much discount in percentage: "))
dis=cp*discount/100
sp=cp-dis
print("Selling price of book: ",sp)