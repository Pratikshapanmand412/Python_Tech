#Input 5 subject marks from user and display grade.(e.g.First class,...)
m1 = int(input("Enter first subject marks:"))
m2 = int(input("Enter second subject marks:"))
m3 = int(input("Enter third subject marks:"))
m4 = int(input("Enter fourth subject marks:"))
m5 = int(input("Enter fifth subject marks:"))
total = m1 + m2 + m3 + m4 + m5
percen = total / 500 * 100
print("Percentage: ",percen)
if(percen >= 70):
    print("you got first class with distinction .....")
elif(percen < 70 and percen >= 60):
    print("you got first class.....")
elif(percen < 60 and percen >= 50):
    print("you got second....")
elif(percen < 50 and percen >= 40):
    print("you got pass class...")
else:
    print("you are fail...")