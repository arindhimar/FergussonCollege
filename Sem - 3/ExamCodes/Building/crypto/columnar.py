plainText="This is as simple as this can be"

key=[5,2,1,3,4]

newPT=[ch for ch in plainText if ch!=" "]

# print(newPT)

l=len(key)

enc={}

for i in range(l):
    enc[key[i]]=""
    

j=0

# print(len(newPT))

for i in range(len(newPT)):
    enc[key[j]]+=newPT[i]
    j=(j+1)%l
    

encStr = ""
for k in sorted(enc):
    encStr += enc[k]

print(encStr)

