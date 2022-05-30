#Input
file = open("C:/Users/91884/AppData/Local/Programs/Python/Python310/XII/Report File/Codes/Files/File5.txt", "r")
#Write only file name

txt = file.read()
vowel = ["A", "E", "O", "I", "U"]
up_count, low_count, con_count, vow_count = 0, 0, 0, 0

print("File Read:- \n"+txt+"\n")

#Loop will check category for each character
for k in txt:
        
    if k.isupper():
        up_count += 1

        if k not in vowel:
            con_count += 1
        
    elif k.islower():
        low_count += 1
        
        if k.upper() not in vowel:
            con_count += 1
            
    if k.upper() in vowel:
            vow_count += 1
            
#Output
print("Total no. of uppercase characters are- ",up_count)
print("Total no. of lowercase characters are- ", low_count)
print("Total no. of consonants are- ", con_count)
print("Total no. of vowels are- ",vow_count)



