pt="thisisasentencethatiwanttoencrypt"

key=[2,3,1,5,4]

enc={}

for i in key:
    enc[i]=""
    

j=0

for ch in pt:
    enc[key[j]]+=ch
    j=(j+1)%(len(key))


# print(enc)
encStr=""
for i in key:
    encStr+=enc[i]
    
print(encStr)