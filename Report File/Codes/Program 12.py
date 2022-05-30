import pickle
record = []
while True:
    roll_no = input("Enter the roll no: ")
    name = input("Enter the name: ")
    marks = input("Enter the marks: ")
    data = [roll_no, name, marks]

    record.append(data)

    a = input("Want to have more inputs(y/n): ")
    if a.upper() == "N":
        break

f= open("List.dat", "wb")
pickle.dump(record, f)
f.close()
print("\nOriginal Record is", record)

f1 = open("List.dat", "rb")
txt = pickle.load(f1)

roll = input("\nEnter the roll no to be updated: ")

for i in range(len(txt)):
        if txt[i][0] == roll:
            marks = input("Enter the new marks to be entered: ")
            txt[i][2] = marks

f1.close()
f2 = open("List.dat", "wb")
pickle.dump(txt, f2)
f2.close()
print("\nUpadted record is", txt)    
