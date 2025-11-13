plainText="ashdahskdhaskhdkajksdh"

key=[5,2,3,4,1]

enc={}

for i in key:
    enc[i]=""
    
    
print(enc)

j=0

for i in range(len(plainText)):
    enc[key[j]]+=plainText[i]
    j=(j+1)%(len(key))
    
print(enc)

encStr = ""
for k in sorted(enc):
    encStr += enc[k]
    
print(encStr)

