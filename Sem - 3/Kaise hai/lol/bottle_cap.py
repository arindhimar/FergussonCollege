li = ["1b", "2c", "1c", "3c", "2b"]

l=len(li)

pair={}

for i in range(l):
    temp=[ch for ch in li[i]]
    if temp[1] == 'b':
        tempL=max(0,i-3)
        tempR=min(l,i+4)
        
        for j in range(tempL,tempR):
            tempC = [ch for ch in li[j]]
            if tempC[1]=='c' and tempC[0] ==temp[0] and li[j] not in pair.values():
                pair[li[i]]=li[j]
                break

print(pair)