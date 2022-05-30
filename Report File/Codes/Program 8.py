file = open("C:/Users/91884/AppData/Local/Programs/Python/Python310/XII/Report File/Codes/Files/File5.txt", "r")
#Write only file name

while True: #Loop will go through all the lines

    line = file.readline()
    
    if not line:
        break #It will break the loop will when readline() function won't return any line
    
    lst = line.split(" ") #Spliting into words
    for l in lst: 
        print(l, end= "#") #Print while separated with #
