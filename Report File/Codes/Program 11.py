import pickle

file = open("BinFile.dat", "wb")
d = {1: "Aakarsh", 2: "Aman", 3: "Arpit", 4: "Karan", 5: "Prakhar"}

pickle.dump(d, file)

file.close()

roll = int(input("Enter roll no to be searched: "))
file1 = open("BinFile.dat", "rb")

b = False

f = pickle.load(file1)
for i in f:
    if i == roll:
        print("Name of roll no",i, "is",f[i])
        b = True
if b == False:
    print("Roll not found")
        
        
        
