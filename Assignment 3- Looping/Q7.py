#WAP to print first 50 prime numbers.
n= 2
c= 0
while(c<=50):
    for j in range(2,n):
        if(n % j ==0):
            break
    else:
        print(n,end=" ")
        c = c+ 1
    n = n+ 1