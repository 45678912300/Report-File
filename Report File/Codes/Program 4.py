n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

fact =1
sum = 0

for i in range(1, n+1):
    fact = fact * i
    if  i % 2 == 0:
         sum += (x**i)/(fact)
    else:
        sum -= (x**i)/(fact)

print("Sum of the series will be", sum)
