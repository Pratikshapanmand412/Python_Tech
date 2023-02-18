#python program to find the second largest number in the list using bubble sort.
data = [34,21,56,78,90,43,100,200]
smax = 0
max = data[0]
n = len(data)
for j in range(1,n):
    for i in range(0,n-j):
        if data[i] > data[i+1]:
            data[i],data[i+1] = data[i+1],data[i]
for i in range(1,n):
    if max < data[i]:
        smax = max
        max= data[i]
    elif smax < data[i]:
        smax=data[i]
print("Second largest number is:",smax)