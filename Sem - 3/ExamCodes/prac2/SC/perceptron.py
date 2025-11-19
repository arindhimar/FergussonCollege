x=[[0,0],[0,1],[1,0],[1,1]]

y=[0,1,1,1]

b=0
lr=0.1

w=[0,0]

ep=10

def d(net):
    if net>=1:
        return 1
    else: 
        return 0

for i in range(ep):
    for j in range(len(x)):
        net=x[j][0]*w[0]+x[j][1]*w[1]+b
        op=d(net)
        
        error=y[j]-op
        
        w[0]+=lr*x[j][0]*error
        w[1]+=lr*x[j][1]*error
        b+=lr*error
        
print(w,b)


