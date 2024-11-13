fileObj = open("file1.txt","r")

# print(fileObj.read().split(" "))

content = fileObj.read().split(" ")

dict ={}

for temp in content:
    if temp not in dict:
        dict[temp] = 1
    else:
        dict[temp] +=1

print(sorted(dict.items(),key = lambda x:x[1],reverse=True))

