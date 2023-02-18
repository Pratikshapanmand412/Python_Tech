#WAP to find a second largest element in the list.
data = [10,23,45,67,78,90,100,110]
max = data[0]
smax = 0
for i in range (1,len(data)):
    if max < data[i]:
        smax = max
        max=data[i]
    elif smax < data[i]:
        smax = data[i]
print("Second largest element is: ",smax)