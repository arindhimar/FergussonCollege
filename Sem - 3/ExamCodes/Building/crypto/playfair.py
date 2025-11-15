def find_pos(ch):
    for r in range(5):
        for c in range(5):
            if mtrx[r][c] == ch:
                return r, c
    return None, None


chars="abcdefghiklmnopqrstuvwxyz"

key="monarchy"


key_unique = ""
for ch in key:
    if ch not in key_unique:
        key_unique += ch
        
combined = key_unique
for ch in chars:
    if ch not in combined:
        combined += ch


mtrx=[]

mtrx.append([combined[i] for i in range(0,5) ])
mtrx.append([combined[i] for i in range(5,10) ])
mtrx.append([combined[i] for i in range(10,15) ])
mtrx.append([combined[i] for i in range(15,20) ])
mtrx.append([combined[i] for i in range(20,25) ])

# print(mtrx)


pt1 = "attack"
pt1 = pt1.replace("j", "i")  
pt1 = pt1.lower()

i=0

tempL=[]


while i < len(pt1):
    if i == len(pt1) - 1:  
        tempL.append([pt1[i], 'x'])
        break
    elif pt1[i] == pt1[i + 1]:  
        tempL.append([pt1[i], 'x'])
        i += 1
    else:
        tempL.append([pt1[i], pt1[i + 1]])
        i += 2

print(tempL)


encText=""

for pair in tempL:
    c1, c2 = pair
    r1, c1pos = find_pos(c1)
    r2, c2pos = find_pos(c2)

    if r1 == r2:  
        encText += mtrx[r1][(c1pos + 1) % 5]
        encText += mtrx[r2][(c2pos + 1) % 5]
    elif c1pos == c2pos:  
        encText += mtrx[(r1 + 1) % 5][c1pos]
        encText += mtrx[(r2 + 1) % 5][c2pos]
    else: 
        encText += mtrx[r1][c2pos]
        encText += mtrx[r2][c1pos]

print(encText)