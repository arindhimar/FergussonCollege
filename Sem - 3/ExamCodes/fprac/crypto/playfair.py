key="sadasda"
alpha="abcdefghiklmnopqrstuvwxyz"

new_key=key.replace("j","i")

finalKey=""

for ch in new_key:
    if ch not in finalKey:
        finalKey+=ch
        

for ch in alpha:
    if ch not in finalKey:
        finalKey+=ch


# print(finalKey)



tempSet=[]

tempSet.append([finalKey[ch] for ch in range(0,5)])
tempSet.append([finalKey[ch] for ch in range(5,10)])
tempSet.append([finalKey[ch] for ch in range(10,15)])
tempSet.append([finalKey[ch] for ch in range(15,20)])
tempSet.append([finalKey[ch] for ch in range(20,25)])

# print(tempSet)

pt="thisiswhatss"

l=len(pt)

# print([ch for ch in pt if ch!='t'])

i=0

tempPair=[]

while i<l:
    if i==l-1:
        tempPair.append([pt[i],'x'])
        break
    elif pt[i]==pt[i+1]:
        tempPair.append([pt[i],'x'])
        i=i+1
    else:
        tempPair.append([pt[i],pt[i+1]])
        i=i+2
    

# print(tempPair)

def findPos(ch):
    for i in range(5):
        for j in range(5):
            if tempSet[i][j]==ch:
                return i,j


encStr=""
    
    
for p in tempPair:
    ch1=p[0]
    ch2=p[1]
    r1,c1=findPos(ch1)
    r2,c2=findPos(ch2)

    if c1==c2:
        encStr+=tempSet[(r1+1)%5][c1]
        encStr+=tempSet[(r2+1)%5][c2]
    elif r1==r2:
        encStr+=tempSet[r1][(c1+1)%5]
        encStr+=tempSet[r2][(c2+1)%5]
    else:
        encStr+=tempSet[r1][c2]
        encStr+=tempSet[r2][c1]

print(encStr)

print()