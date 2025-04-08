def game():
    x = 5
    b=4
    a,b=0,0
    g=2
    
    while True:
        print(a,b)
        
        if a==g or b ==g:
            print("win")
            break
        
        print("1-full a \n2-full b\n 3- empty a \n 4- empty b\n 5- a to b\n7-b to a")
        
        ch  = input("select")
        
        if ch =="1": 
            a = x
        elif ch =="2":
            b=y
        elif ch =="3":
            a=0
        elif ch =="4":
            b=0
        elif ch =="5":
            pour = min(a,y-b)
            a-=pour
            b+=pour
        elif ch =="5":
            pour = min(b,x-a)
            a+=pour
            b-=pour
    
game()