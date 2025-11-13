plainText="THis is as asjdkahs as mdbkasd ams das d asadnkasn"

lowerPlainText=plainText.lower()

key=126

enc=""

for ch in lowerPlainText:
    if ch.isalpha():
        enc+=chr(((ord(ch)-97+key)%26)+97)
    else:
        enc+=ch


print(enc)
        