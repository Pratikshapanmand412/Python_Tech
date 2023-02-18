# WAP to remove duplicates from the list.
list = [1,23,21,12,34,23,1,12,23]
print("Original list is : ",list)
Newlist = []
for i in list:
    if i not in Newlist:
        Newlist.append(i)

print("list after removing duplicates: ",Newlist)