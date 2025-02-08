import os

f = open("aurEknew.txt","r")

strName = input("Enter name for the file")

f2 = open(strName+".txt","w")

strData = f.read()

f2.write(strData)

f.close()
f2.close()