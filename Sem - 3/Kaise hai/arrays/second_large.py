tempL=[1,2,4,7,7,5]

l=len(tempL)

fmax=tempL[0]

for i in range(l):
    if tempL[i]>fmax:
        fmax=tempL[i]

sMax=tempL[0]

for i in range(l):
    if tempL[i]>sMax and tempL[i]<fmax:
        sMax=tempL[i]
        
        
print(sMax)

