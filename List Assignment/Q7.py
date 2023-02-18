#python program to find the intersection of two lists.
list1 = [1,2,3,4,5]
list2 = [2,6,7,8,9,3,4]
newlist = []
for element in list1 :
    if element in list2:
        newlist.append(element)
print("Intersection of two list is:",newlist)