#Accept age of 5 People and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition:
#a.Children below 12= 30% discount
#b.Senior citizen (above 59)=%0% discount
#c.Others need to pay full

age = int(input("Enter your age:"))
tic_amt = float(input("Enter ticket amount: "))
if(age <= 12):
    dis = tic_amt * 0.30
    total_amt = tic_amt - dis
    print("You have to pay:",total_amt)
elif(age >= 59):
    dis = tic_amt * 0.50
    total_amt = tic_amt - dis
    print("You have to pay: ",total_amt)
else:
    print("You have to pay full amount: ",tic_amt)