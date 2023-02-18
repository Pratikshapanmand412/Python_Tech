#WAP to reverse the list.
data = [1,3,8,14,34,45,100]
l =len(data)
for i in range (int(l / 2)):
    n = data[i]
    data[i] = data[l - i - 1]
    data [l - i -1] = n
print(data)