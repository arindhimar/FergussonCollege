import rsa

pb,pt=rsa.newkeys(2048)

password="asdjkjajskdhaskhd"

ct=rsa.encrypt(password.encode(),pb)

print(ct)

p=rsa.decrypt(ct,pt).decode()

print(p)