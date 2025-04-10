def game():
    x=5
    y=4
    a,b=0,0
    
    g=2
    
    while True:
        print(a,b)
        
        if a==g:
            print("win")
            
        print("1- fill a \n2-fill b \n3-empty a\n4-empty b\n5-pour a to b\n6-pour b to a")
        
        ch = input("\nselect  ")
        
        if ch  == "1":a=x
        elif ch =="2": b=y
        elif ch =="3": a=0
        elif ch =="4": b=0
        elif ch =="5":
            pour = min(a,y-b)
            a-=pour
            b+=pour
        elif ch =="6":
            pour = min(bv,x-a)
            a+=pour
            b-=pour
            

game()
        