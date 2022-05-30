#Input
file = open("C:/Users/91884/AppData/Local/Programs/Python/Python310/XII/Report File/Codes/Files/File4.txt", "r")
#Write only file name
fill = open("C:/Users/91884/AppData/Local/Programs/Python/Python310/XII/Report File/Codes/Files/File6.txt", "w")

st = ""
while True: #This loop will check through whole file
    
    f = file.readline() #It will read each line individually 
    if not f:
        break #Loop will break when no line is read

    st = ""
    s = True #Defining condition for a not found

    for ch in f:
        if ch.upper() == "A": #"a" found!
            s = False
            
    if s ==  True:
        st = st + f #storing leftover lines in a string

fill.write(st) #It will write string in a new file
file.close()
fill.close()
