s = "BAABAABBBAAA"
k = 2

l = len(s)
maxLen = 0

for i in range(l):
    tempK = 0
    tempL = 0
    ch = s[i] 
    for j in range(i, l):
        if s[j] != ch:
            if tempK < k:
                tempK += 1
                tempL += 1
            else:
                break
        else:
            tempL += 1
        maxLen = max(maxLen, tempL)

print(maxLen)
