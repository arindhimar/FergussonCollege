def isValid(mleft,cleft,mright,cright):
    if mleft<0 or cleft <0 or mright<0 or cright<0:
        return False
    
    if mleft>0 and cleft>mleft:
        return False
    if mright>0 and cright>mright:
        return False

    return True


def game():
    left = [3,3]
    right=[0,0]
    
    boat = "left"
    
    while True:
        print(left,right,boat)
        
        if right == [3,3]:
            print("win")
            break

        try:
            m = int(input("enter m"))
            c = int(input("enter c"))
        except:
            continue
        

        if m+c ==0 or m+c >2:
            continue
        
        if boat == "left":
            if m>left[0] or c>left[1]:
                continue
            
            newleft = [left[0]-m,left[1]-c]
            newright = [right[0]+m,right[1]+c]
        else:
            if m>right[0] or c>right[1]:
                continue
            newleft = [left[0]+m,left[1]+c]
            newright = [right[0]-m,right[1]-c]
            
        
        if not isValid(newleft[0],newleft[1],newright[0],newright[1]):
            continue
        
        left,right = newleft,newright
        
        if boat =="left":
            boat = "right"
        else:
            boat = "left"
            


game()
            
        
    