from simplecrypt import encrypt, decrypt

text="asdjkahsjdaskhd"
password = "mysecret"

cipher = encrypt(password, text)


decrypted = decrypt(password, cipher)

print(decrypted)