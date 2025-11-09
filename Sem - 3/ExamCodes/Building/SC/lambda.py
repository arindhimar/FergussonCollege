l = [
    [0.3, 0.7],
    [0.5, 0.2],
    [0.9, 0.4]
]

lb=0.3

for i in range(3):
    for j in range(2):
        if l[i][j]>=lb:
            l[i][j]=1
        else:
            l[i][j]=0

print(l)