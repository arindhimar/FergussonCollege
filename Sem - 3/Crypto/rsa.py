import rsa

(pubkey, privkey) = rsa.newkeys(2048)

password = input("Enter password to encrypt: ")
ciphertext = rsa.encrypt(password.encode(), pubkey)
print("Ciphertext (bytes):", ciphertext)

with open("pwd_encrypted.bin", "wb") as f:
    f.write(ciphertext)

plain = rsa.decrypt(ciphertext, privkey).decode()
print("Decrypted password:", plain)
