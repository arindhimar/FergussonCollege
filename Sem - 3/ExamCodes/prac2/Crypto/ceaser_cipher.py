pt="ashdkashdjkahsdja"
key=3

encStr=""

for ch in pt:
    encStr+=chr((((ord(ch)-97)+key)%26)+97)
    

print(encStr)