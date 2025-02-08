def menu():
    print("1 - Write")
    print("2 - Read")
    print("3 - WriteLine")
    print("4 - ReadLine")

opt = True

while opt:
    fileObj = open("file1.txt","r+")
    menu()
    sel = int(input("Select Option "))
    if sel == 1:
        str = input("Write something to add in the file")
        fileObj.write(str)
    elif sel==2:
        print(fileObj.read())
    elif sel==3:
        str = input("Write something to add in the file")
        fileObj.writelines(str)
    elif sel==4:
        print(fileObj.readline())
    else:
        opt = False
        
    
    
    