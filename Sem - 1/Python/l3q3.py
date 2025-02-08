def list_multiply(tempList):
    prod=1
    for i in tempList:
        prod  = prod * i
    return prod

print(list_multiply([1,2,3,4,5,6,7,8,9,10]))