
while(1):
    
    print("1 +")
    print("2 -")
    print("3 *")
    print("4 /")
    print("5 **")
    print("6 //")
    
    
    
    opt = int(input("Select the operation       "))
    
    n1 = int(input("number 1"))
    n2 = int(input("number 2"))
    
    if opt ==1 :
        print(n1+n2)
    elif  opt ==2 :
        print(n1-n2)
    elif  opt ==3 :
        print(n1*n2)
    elif  opt ==4 :
        print(n1/n2)
    elif  opt ==5 :
        print(n1**n2)
    elif  opt ==6 :
        print(n1//n2)
    else:
        print("wrong option!!")
    
    
    
    tempRun = input("enter false to exit")
    if tempRun.lower() == "false":
        break
    
    