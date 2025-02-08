def dictFun(**args):
    for temp in args:
        print(temp)
        

tempDict = {"name":"arin","idk":"yes"}

dictFun(**tempDict)