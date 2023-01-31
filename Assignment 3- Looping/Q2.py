#Enter number of students from user.For those many students accept marks of 5 subjects 
#marks from user and calculate percentage.Display all percentage and average percentage of students.
students = int(input("Enter number of students: "))

for i in range(1,students + 1):
    m1 = int(input("Enter marks of first subject: "))
    m2 = int(input("Enter marks of second subject: "))
    m3 = int(input("Enter marks of third subject: "))
    m4 = int(input("Enter marks of fourth subject: "))
    m5 = int(input("Enter marks of fifth subjects: "))

    total = m1 + m2 + m3 + m4 + m5
    percen = total / 500 * 100
    print("Percentage:",percen)

average=percen /1500
print(average)