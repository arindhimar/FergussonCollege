plainText="THis is as asjdkahs as mdbkasd ams das d asadnkasn"

lowerPlainText=plainText.lower()

print(lowerPlainText)

key=[1,2,3,4,5]

l=len(key)

enc=""

i=0

for ch in lowerPlainText:
    if ch.isalpha():
        new_ch = chr(((ord(ch) - 97 + key[i]) % 26) + 97)
    else:
        new_ch=ch
    
    enc+=new_ch
    
    i=(i+1)%l
    
print(enc)
