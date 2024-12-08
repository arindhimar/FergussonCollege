f = open("i.txt","r")

# print(f.readlines())
    
data = f.read()

tempStr=""

countdir={}

for temp in data:
    if temp == " " or temp =="\n":
        if tempStr in countdir.keys():
            countdir[tempStr]+=1
        else:
            countdir[tempStr]=1
        tempStr=""
    else:
        tempStr+=temp
        
print(countdir)