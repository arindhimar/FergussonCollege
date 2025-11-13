plainText = "hello world"
password = "xmcklzptqwe"


plainText = plainText.lower()
password = password.lower()


enc = ""
for p, k in zip(plainText, password):
    if p.isalpha():
        enc += chr(((ord(p) - 97 + ord(k) - 97) % 26) + 97)
    else:
        enc += p

print(enc)


dec = ""
for c, k in zip(enc, password):
    if c.isalpha():
        dec += chr(((ord(c) - 97 - (ord(k) - 97)) % 26) + 97)
    else:
        dec += c

print(dec)
