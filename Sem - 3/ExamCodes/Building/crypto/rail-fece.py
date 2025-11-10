plainText="ashdahskdhaskhdkajksdh"

depth=3

enc={}

for i in range(3):
    enc[i]=""
    

l=len(plainText)

sign="+"

j=0

for i in range(l):
    enc[j]+=plainText[i]
    
    if sign =="+":
        if j==depth-1:
            sign="-"
            j-=1
        else:
            j+=1
    else:
        if j==0:
            sign="+"
            j+=1
        else:
            j-=1
    

encStr=""

for i in range(depth):
    encStr+=enc[i]
    
print(encStr)

