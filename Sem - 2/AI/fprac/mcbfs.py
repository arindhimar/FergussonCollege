from collections import deque

def isvalid(mleft,cleft,mright,cright):
    if mleft<0 or cleft<0 or mright <0 or cright<0:
        return False
    
    if mleft>0 and cleft>mleft:
        return False
        
    if mright>0 and cright>mright:
        return False
        
    return True

def bfs():
    start = (3,3,1)
    goal = (0,0,0)
    
    q = deque()
    v = set()
    
    q.append((start,[start]))
    v.add(set)
    
    while q:
        (mleft,cleft,boat),path = q.popleft()
        
        mright = 3 - mleft
        cright = 3 - cleft
        if (mleft,cleft,boat) == goal:
            print("won")
            for p in path:
                print(p)
                
            break
        
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        
        for mmove,cmove in moves:
            if boat ==1:
                newstate = (mleft-mmove,cleft-cmove,0)
            else:
                newstate = (mleft+mmove,cleft+cmove,1)
            
            newmleft,newcleft,newboat = newstate
            
            newmright = 3-newmleft
            newcright = 3 - newcleft
            
            if isvalid(newmleft,newcleft,newmright,newcright) and newstate not in v:
                q.append((newstate,path+[newstate]))
                v.add(newstate)
                


bfs()
                
        
        
        