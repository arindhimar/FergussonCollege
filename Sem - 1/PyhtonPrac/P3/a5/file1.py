f = open("i.txt","r")

# print(f.read())
temp = f.read()
f.close()

f = open("f.txt","w")
f.write(temp[::-1])

f.close()


