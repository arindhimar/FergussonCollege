f = open("newWalahaiyeh.txt","r+")


str = f.read()

f = open("newWalahaiyeh.txt","w")


f.write(str[::-1])


f.close()