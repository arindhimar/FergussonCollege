from collections import deque

def bfs():
    maxa=5
    maxb=4
    goal=2
    
    queue  =deque()
    
    visited = set()
    
    queue.append((0,0))
    visited.add((0,0))
    
    while queue:
        a,b = queue.popleft()
        
        print(a,b)
        
        if a ==goal:
            print("woon")
            break
        
        moves = [(maxa,0),(a,maxb),(0,b),(a,0),(a-min(a,maxb-b),b+min(a,maxb-b)),(a+min(b,maxa-a),b-min(b,maxa-a))]   
        
        for move in moves:
            if move not in visited:
                queue.append(move)
                visited.add(move)
                
                

bfs()
        