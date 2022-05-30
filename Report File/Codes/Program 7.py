dic = {}

n = int(input("Enter the number of students: "))

for i in range(1, n+1):
    roll_no = input("Enter the roll no of the student: ")
    name = input("Enter the name of the student: ")
    marks = int(input("Enter the marks of the student: "))

    dic[(roll_no)] = (name, marks)

print("\nCongratulations! The following students have scored above 75.")
for k in dic:
    if dic[k][1] >= 75:
        print(dic[k][0])
