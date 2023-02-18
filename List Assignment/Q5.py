#python program to sort a list according to the length of the elements within the list.
list = []
n = int(input("Enter a number of elements: "))
for i in range(1, n +1):
    b = input("Enter a element :")
    list.append(b)
list.sort(key = len)
print(list)