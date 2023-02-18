#python program to find the union of two lists.

list1 = []
num1 = int(input("Enter size of list: "))
for n in range(num1):
    element = int(input("Enter any numbers :"))
    list1.append(element)

list2 = []
num2  = int(input("Enter a size of list2 : "))
for n in range(num2):
    element2 = int(input("Enter any number : "))
    list2.append(element2)
union = list(set().union(list1,list2))
print("The union of two lists is: ",union)