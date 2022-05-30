import csv

fields = ["User ID", "Password"]

n = int(input("How many rows you want to store: "))
rows = []

for i in range(n):
    lst = []
    
    user = input("\nEnter the user id of user: ")
    password = input("Enter the password of user: ")

    lst = [user, password]
    rows.append(lst)
    
file = open("Data.csv", "w")

write = csv.writer(file, delimiter = ",")
write.writerow(fields)

write.writerows(rows)

file.close()

user = input("\nEnter the user id of user whose password to be given: ")
f1 = open("Data.csv", "r")
read = csv.reader(f1)

for row in read:
    if len(row) == 0:
        continue
    else:
        if row[0] == user:
            print("The password of", user,"is",row[1])

