import rsa

(pb,ptk)=rsa.newkeys(2048)

pt="asdjkashkdghas"

cipher=rsa.encrypt(pt.encode(),pb)

plain=rsa.decrypt(cipher,ptk).decode()


print(plain)