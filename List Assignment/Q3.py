#python program to sort list according to second element in sublist.
list = [[1,2],[2,1],[3,3]]
for i in range (0,len(list)):
    for j in range(0,len(list)- i -1):
        if (list[j][1] > list[j + 1][1]):
            temp = list[j]
            list[j ]= list[j + 1]
            list[ j + 1] = temp
print(list)