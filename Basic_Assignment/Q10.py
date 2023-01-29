#WAP to calculate  total salary of employee based on basic,da=10% of basic,
# ta=12% of basic,hra=15% of basic 
basic=float(input("Enter basic salary of employee: "))
da=basic*0.10
ta=basic*0.12
hra=basic*0.15
total_salary=basic+da+ta+hra
print("Total salary of employee is :",total_salary)