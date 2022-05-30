def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

def LCM(x, y):
    if x % y == 0:
        return x
    else:
        return  int(x * LCM(y, x % y)/(x %y))
    
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD of the numbers is", str((GCD(x, y)))+".")
print("LCM of the numbers is", str((LCM(x, y)))+".")
