#WAP to create a new list from existing list which contains cube of each number of list
data = [1,2,4,5,3,11,8]
newlist = []
for x in data:
    newlist.append(x**3)
print(newlist)