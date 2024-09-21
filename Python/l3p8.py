def changeOccurence(tempString):
    toChange = tempString[0]
    newString = list(tempString)  
    for i in range(len(tempString)):
        if newString[i] == toChange:
            newString[i] = '@'
    return ''.join(newString)  


print(changeOccurence("aarin"))