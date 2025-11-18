from simplecrypt import encrypt,decrypt

u="arin"
p="dhimar"

ct=encrypt(p,u)
pt=decrypt(p,ct)

print(ct,pt)