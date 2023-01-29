#WAP to accept an integer amount from user and tell minimum number of notes
#needed for representing that amount.
n = int(input("Enter amount: "))
n1 = n // 2000
r1 = n % 2000
if(r1>=1000):
    n2 = r1 // 1000
    r2 = r1 % 1000
else:
    n2 = r1 // 500
    r2 = r1 % 500
if(r2>=100):
    n3 = r2 // 100
    r3 = r2 % 100
else:
    n3 = r2 // 50
    r3 = r2 %  50
if(r3>=50):
    n4 = r3 //50
    r4 = r3 % 50
else:
    n4 = r3 // 10
    r4 = r3 % 10
if(r4>=10):
    n5 = r4 // 10
    r5 = r4 % 10
else:
    n5 = r4 // 5
    r5 = r4 % 5

total_notes = n1 + n2 + n3 + n4 + n5
print("Total number of notes : ",total_notes)





