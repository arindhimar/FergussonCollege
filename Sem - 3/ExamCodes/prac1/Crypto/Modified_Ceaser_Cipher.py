plainText="THis is as asjdkahs as mdbkasd ams das d asadnkasn"

lowerPlainText=plainText.lower()

key=[1,2,3,4,5]

l=len(key)

enc=""

j=0

for ch in lowerPlainText:
    if ch.isalpha():
        enc+=chr(((ord(ch)-97+key[j])%26)+97)
        j=(j+1)%l
    else:
        enc+=ch


print(enc)
dec=""
j=0
for ch in enc:
    if ch.isalpha():
        dec+=chr(((ord(ch)-97-key[j])%26)+97)
        j=(j+1)%l
    else:
        dec+=ch
        
print(dec)
