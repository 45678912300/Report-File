a = "y"
while True:
    n = int(input("Enter a number: "))

    s = False

    for i in range(2, n):
        if n % i == 0:
            s = True

    if s:
        print(n,"is not a prime.")
    else:
        print(n,"is a prime number.")
        
    a = input("Do you want more numbers(y/n): ")
    if a.upper() == "N":
        break
