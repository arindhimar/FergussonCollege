
# pip install simple-crypt

from simplecrypt import encrypt, decrypt
import hashlib
import base64

text = input("Enter the text: ")
password = "mysecret"

#q1 - Symmetric Encryption/Decryption
cipher = encrypt(password, text)
print("\nEncrypted (bytes):", cipher)

decrypted = decrypt(password, cipher).decode("utf-8")
print("Decrypted text:", decrypted)

#q2 - Message Digests
md5_hash = hashlib.md5(text.encode()).hexdigest()
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("\nMessage Digests:")
print("MD5   :", md5_hash)
print("SHA1  :", sha1_hash)
print("SHA256:", sha256_hash)

#q3 - Base64 Encoding/Decoding
encoded = base64.b64encode(text.encode())
decoded = base64.b64decode(encoded).decode("utf-8")

print("\nBase64 Encoding/Decoding:")
print("Encoded:", encoded)
print("Decoded:", decoded)
