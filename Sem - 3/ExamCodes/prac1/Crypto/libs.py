# from simplecrypt import encrypt, decrypt
from hashlib import md5,sha256


text="asdjkahsjdaskhd"
password = "mysecret"

# cipher = encrypt(password, text)

# deCiper=decrypt(password,cipher)

print(md5(text.encode()).hexdigest())
print(sha256(text.encode()).hexdigest())