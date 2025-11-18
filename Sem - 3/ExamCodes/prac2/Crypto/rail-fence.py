k=3

sign="+"

pt="arindhimar"

enc={}
for i in range(k):
    enc[i]=""
    

print(enc)

j=0
for ch in pt:
    enc[j]+=ch
    
    if sign=="+":
        if j==k-1:
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
            

# print(enc)

encStr=""

for i in range(k):
    encStr+=enc[i]


print(encStr)