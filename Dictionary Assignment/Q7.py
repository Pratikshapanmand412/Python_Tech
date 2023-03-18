#Program to remove the given key from a dictionary.
d = {'a':1 , 'b':2 , 'c':3 ,'d':4}
print("original dictionary :", d)
key = (input("Enter the key to remove: "))
if key in d:
    del d[key]
else:
    print("key not found")
    exit(0)
print("After removing key dictionary is: ",d)