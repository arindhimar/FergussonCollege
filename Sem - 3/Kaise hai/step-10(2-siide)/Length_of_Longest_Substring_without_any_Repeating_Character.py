s = "abcabcbb"


n=len(s)

maxLen=0
tempLen=0


for i in range(n):
    ns=""
    dict={}
    tempLen=0
    for j in range(i,n):
        if s[j] in dict:
            break

        dict[s[j]]=True
        ns+=s[j]
        tempLen+=1
        maxLen=max(maxLen,tempLen)