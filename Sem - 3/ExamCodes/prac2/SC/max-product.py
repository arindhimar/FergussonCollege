r1=c1=r2=c2=3

l1=[[0.2,0.4,0.6],
    [0.1,0.3,0.5],
    [0.7,0.8,0.9]]

l2=[[0.5,0.3,0.2],
    [0.6,0.4,0.1],
    [0.9,0.8,0.7]]


matrix=[]

for i in range(r1):
    row=[]
    for j in range(c2):
        temp=[]
        for k in range(c1):
            temp.append(l1[i][k]*l2[k][j])
            
        row.append(max(temp))
    matrix.append(row)
    
    
print(matrix)