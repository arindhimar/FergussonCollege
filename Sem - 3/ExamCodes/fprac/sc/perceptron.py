x=[[0,0],[0,1],[1,0],[1,1]]
y=[0,1,1,1]  

b=0.0
lr=0.1

w=[0.0,0.0]

def step_function(z):
    if z>=0:
        return 1
    else:
        return 0
    
    

epochs=10

for eppoch in range(epochs):
    for i in range(len(x)):
        z=w[0]*x[i][0]+w[1]*x[i][1]+b
        pred=step_function(z)
        
        error=y[i]-pred
        
        w[0]=w[0]+lr*error*x[i][0]
        w[1]=w[1]+lr*error*x[i][1]
        b=b+lr*error
        

print("Weights:",w)
print("Bias:",b)
