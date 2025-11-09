import rsa

(pubkey, privkey) = rsa.newkeys(2048)

password = input("Enter password to encrypt: ")


ciphertext = rsa.encrypt(password.encode(), pubkey)


print("Ciphertext (bytes):", ciphertext)


plain = rsa.decrypt(ciphertext, privkey).decode()


print("Decrypted password:", plain)