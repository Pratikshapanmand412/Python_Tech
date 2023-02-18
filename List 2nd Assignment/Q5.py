# Accept number from user and check if this element is present in the list or not.Also tell how many times it is present in the list.
data = [1,12,23,43,54,5,7,87,12,1,23,1,12,12]
n=int(input("Enter a number: "))
count=0
for x in data:
    if x == n :
        count += 1
    
print("Number is present count is: ",count)



