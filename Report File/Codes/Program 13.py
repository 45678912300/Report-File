import random

a = "y"
while a == "y":
    x = random.randint(1, 6)
    print(x)
    
    a = input("Do you want more numbers(y/n): ")
