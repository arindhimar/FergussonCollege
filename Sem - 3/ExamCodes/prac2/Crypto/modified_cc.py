pt="ashdkashdjkahsdja"
key=[2,2,4,2,1]

encStr=""

j=0

for ch in pt:
    encStr+=chr((((ord(ch)-97)+key[j])%26)+97)
    j=(j+1)%len(key)    

print(encStr)