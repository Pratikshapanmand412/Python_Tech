#b.N + N^2 +N^3.....+N^N(exponent)
n = int(input("Enter a number: "))
power = 0
for i in range(1,n+1):
    power += n ** i
print("Result:",power)
