tp = ()

a = "y"
while a == "y":
    n = input("Enter an element: ")
    tp = tp + (n,)

    a = input("Do you want more inputs(y/n): ")
    
x = input("\nEnter an element to be searched: ")
s = False
for i in tp:
    if i == x:
        s = True
if s:
    print(x, "Found! at index", tp.index(x))
else:
    print("Sorry! Element not found")
