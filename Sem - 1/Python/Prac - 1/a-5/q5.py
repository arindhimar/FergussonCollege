fileObj = open("file1.txt","r+")

content = fileObj.readline()

# print(content[::-1])

fileObj.writelines(content[::-1])