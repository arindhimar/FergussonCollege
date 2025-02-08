def operations():
    print("1 - +")
    print("2 - -")
    print("3 - *")
    print("4 - /")
    print("5 - **")
    print("6 - //")
    
opt = True

while(opt):
    operations();
    opr = int(input("Enter option"))
    
    a = int(input("Enter variable a "))
    b = int(input("Enter variable b "))
    
    if opr == 1 :
        print(str(a)+"+"+str(b)+"="+str(a+b))
    elif opr == 2:
        print(str(a)+"-"+str(b)+"="+str(a-b))
    elif opr == 3:
        print(str(a)+"*"+str(b)+"="+str(a*b))
        
    elif opr == 4:
        print(str(a)+"/"+str(b)+"="+str(a/b))
    elif opr == 5:
        print(str(a)+"**"+str(b)+"="+str(a**b))
        
    elif opr == 6:
        print(str(a)+"//"+str(b)+"="+str(a//b))
    else:
        opt = False    
    
