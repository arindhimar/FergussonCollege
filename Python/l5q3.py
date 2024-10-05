import os

def menu():
    print(" 1 - Open")
    print(" 2 - Write")
    print(" 3 - Read")
    print(" 4 - WriteLine")
    print(" 5 - ReadLine")
    print(" 6 - Close")
    print(" 7 - Rename")
    print(" 8 - Exit")
    
    


while(True):
    menu()

    

    
    opt = int(input("Select option from the menu    "))
    f = open("demofile.txt", "a+")
    if(opt == 8):
        exit(0)
        
    if(opt==1):
        f = open("demofile.txt", "a+")
    elif opt==2:
        str = input("Enter data to write to the file")
        f.write(str)
    elif opt==3:
        print(f.read())
    elif opt==4:
        str = input("Enter data to writeline to the file")
        f.writelines(str)
    elif opt==5:
        print(f.readline())
    elif opt==6:
        f.close()
    elif opt==7:
        f.close()
        str = input("Enter name for new file")
        os.rename("demofile.txt",str)
        
    
    
    
    