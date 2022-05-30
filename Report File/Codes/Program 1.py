#Taking Inputs
a = "y"
while True:
    n = int(input("Enter a number: "))
    sum = 0

    #Main Loop
    for i in range(1, n):
        if n % i == 0:
            sum += i

    #Output
    if sum == n:
        print(n,"is a perfect number.")
    else:
        print(n,"isn't a perfect number.")

    #More Inputs
    a = input("Do you want more numbers(y/n): ")
    if a.upper() == "N":
        break

            
