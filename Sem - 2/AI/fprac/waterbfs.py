from collections import deque

def bfs():
    maxa = 5
    maxb=4
    
    goal = 2
    
    
    q = deque()
    v = set()
    q.append((0,0))
    v.add((0,0))
    while True:
        a,b = q.popleft()
        
        print(a,b)
        
        if a ==goal or b == goal:
            print("win")
            break
        
        moves = [(maxa,b),(a,maxb),(0,b),(a,0),(a-min(a,(maxb-b)),b+min(a,(maxb-b))),(a+min(b,(maxa-a)),b-min(b,(maxa-a)))]
        
        for move in moves:
            if move not in v:
                q.append(move)
                v.add(move)
                
                

bfs()
        