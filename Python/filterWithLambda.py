tempList = [5,10,7,4,1,8]

tempFilter = lambda temp:temp>4

print(list(filter(tempFilter,tempList)))