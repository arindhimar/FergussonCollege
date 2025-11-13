r1,c1=2,3

r2,c2=3,2

a=[[1,0.2,0.5],[0.4,0.8,0.7]]
b=[[0.3,0.6],[0.9,0.1],[0.4,0.5]]

res=[]

for i in range(r1):
    row=[]
    for j in range(c2):
        temp=[]
        for k in range(c1):
            temp.append(min(a[i][k],b[k][j]))
        row.append(max(temp))
    res.append(row)
    

print(res)