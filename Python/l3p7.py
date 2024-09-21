def isPerfectNumber(tempNumber):
    sum  = 0
    for i in range(1,tempNumber+1):
        if tempNumber % i == 0:
            sum=sum+i
            
    return sum==tempNumber
            

print(isPerfectNumber(9))