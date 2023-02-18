#WAP to find maximum and minimum elements in a list.
data = [10,12,32,45,60,100,2,111,1,236]
max = data[0]
min = data[0]
for i in range (1,len(data)):
    if max < data[i]:
        max = data[i]
    if min > data[i]:
        min = data[i]

print("maximum: ",max)
print("Minimum: ",min)