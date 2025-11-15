plainText="THis is as asjdkahs as mdbkasd ams das d asadnkasn"

lowerPlainText=plainText.lower()

# print(lowerPlainText)

key=128

enc=""

for ch in lowerPlainText:
    if ch.isalpha():
        new_ch = chr(((ord(ch) - 97 + key) % 26) + 97)
    else:
        new_ch=ch
    
    enc+=new_ch
    
    
print(enc)
