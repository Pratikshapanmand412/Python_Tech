#WAP to reverse a given number using recursive function.
def rev(n,r):
    if(n == 0):
        return r
    else:
        r = r * 10 + n % 10
        n //= 10
        rev(n,r)
n=int(input("Enter a number: "))
r =0
print(rev(n,r))
