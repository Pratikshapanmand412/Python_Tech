#python program to merge two list and sort it.

list1 = [1,2,3,4,5,54,67,100,7,90]
list2 = [20,34,32,12,78]
data = list1 + list2
n = len(data)
for j in range(1,n):
    for i in range(0,n-j):
        if data[i]> data[i+1]:
            data[i],data[i+1] = data[i+1],data[i]
print("Sorted list :",data)
