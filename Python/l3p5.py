def factorial(tempNumber):
    fact = 1
    for i in range(1,tempNumber+1):
        fact = fact *i
    return fact

print(factorial(5))