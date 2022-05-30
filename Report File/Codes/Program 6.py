lst = []
a = "y"

while a == "y":
    x = int(input("Enter a number: "))
    lst.append(x)

    a = input("Do you want more inputs(y/n): ")

print("The largest number in list is", max(lst))
print("The largest number in list is", min(lst))
