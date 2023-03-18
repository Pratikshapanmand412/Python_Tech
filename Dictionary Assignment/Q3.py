#Program to check if a given key Exists in a dictionary or not.
d = {'a':1 ,'b':2, 'c':3} 
key = input("Enter  key to check : ")
if key in d.keys():
    print("key is present & value of key ",d[key])
else:
    print("key isn't present") 