from collections import deque

def isvalid(mleft,cleft,mright,cright):
    if mleft < 0 or cleft < 0 or mright < 0 or cright < 0:
        return False
    
    if mright>0 and cright > mright:
        return False
    
    if mleft > 0 and cleft > mleft:
        return False
        
    return True

def bfs():
    
    start = (3,3,1)
    goal = (0,0,0)
    
    queue = deque()
    visited = set()
    
    queue.append((start,[start]))
    visited.add(start)
    
    while queue:
        (mleft,cleft,boat),path = queue.popleft()
        
        mright = 3 - mleft
        cright = 3 - cleft
        
        if (mleft,cleft,boat)==goal:
            print("DOn")
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
            
            newmright = 3 -newmleft
            newcright = 3 - newcleft
            
            if isvalid(newmleft,newcleft,newmright,newcright) and newstate not in visited:
                visited.add(newstate)
                queue.append((newstate,path+[newstate]))
                
                
bfs()
                