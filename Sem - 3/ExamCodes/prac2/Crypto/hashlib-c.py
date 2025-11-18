from hashlib import md5,sha1,sha256

text="askdjasda"


print(md5(text.encode()).hexdigest())
print(sha256(text.encode()).hexdigest())