s = "ababxyzabababa"

st=s[:2]

newS=s.replace(st,"$")

newF=""

i=0

while i<(len(newS)):
    ch=newS[i]
    newF+=newS[i]
    # print(i)
    if ch=='$':
        
        while newS[i]=='$' and i < len(newS) :
            print(i)
    
            i+=1
    else:
        i+=1
print(newF)