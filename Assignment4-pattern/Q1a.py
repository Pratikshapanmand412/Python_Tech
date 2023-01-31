for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if(j==1 or i==j ):
            print("*  ",end=" ")
        else:
            print("   ",end=" ")
    print()
for i in range(6-1,0,-1):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if(j==1 or i==j ):
            print(" *  ",end="")
        else:
            print("   ",end=" ")
    print()