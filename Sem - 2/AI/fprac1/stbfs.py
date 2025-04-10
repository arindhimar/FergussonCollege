from collections import deque

def bfs():
    maxa=5
    maxb=4
    g=2
    
    q = deque()
    q.append((0,0))
    
    v=set()
    v.add((0,0))
    
    while q:
        a,b=q.popleft()
        
        print(a,b)
        
        if a==g:
            print("win")
            break
        
        moves = [
            (maxa,b),(0,b),(a,0),(a,maxb),(a-min(a,maxb-b),b+min(a,maxb-b)),(a+min(b,maxa-a),b-min(b,maxa-a))
        ]
        
        for move in moves:
            if move not in v:
                q.append(move)
                v.add(move)
                
                

bfs()
        