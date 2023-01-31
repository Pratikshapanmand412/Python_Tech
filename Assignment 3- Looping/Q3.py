#Accept no of passengers from user and per ticket cost .Then accept age of each 
#passenger and then calculate total amount to  ticket to travel for all of them based on following condition:
#a.Children below 12= 30% discount
#b.Senior citizen (above 59)=%0% discount
#c.Others need to pay full

no_of_passenger = int(input("Enter number of passengers: "))
per_tic_cost= int(input("Enter cost of per ticket: "))
final_amt = 0
for i in range(1,no_of_passenger + 1):
    age=int(input("Enter your age:"))
    
    if(age <= 12):
        dis = per_tic_cost * 0.30
        total_amt = per_tic_cost - dis
        print("You have to pay:",total_amt)
        final_amt +=total_amt
        
    elif(age >= 59):
        dis = per_tic_cost* 0.50
        total_amt = per_tic_cost- dis
        print("You have to pay: ",total_amt)
        final_amt += total_amt
else:
    print("You have to pay full amount: ",per_tic_cost)
    final_amt += per_tic_cost

print("Total amount to ticket to travel for all passengers is: ",final_amt)

