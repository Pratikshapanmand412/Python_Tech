#Python program to put Even & Odd elements of list into two different lists.
data = [10,20,34,56,78,90,54,3,9,7]
n=len(data)
even=[]
odd=[]
for a in data:
    if (a % 2==0):
        even.append(a)
    else:
        odd.append(a)
print(even)
print(odd)
