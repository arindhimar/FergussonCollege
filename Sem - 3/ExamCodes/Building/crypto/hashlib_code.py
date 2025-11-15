import hashlib

text="asdjkahsjdaskhd"


md5_hash = hashlib.md5(text.encode()).hexdigest()
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("MD5   :", md5_hash)
print("SHA1  :", sha1_hash)
print("SHA256:", sha256_hash)
