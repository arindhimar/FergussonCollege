isEven = lambda n: n % 2 == 0

tempList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evenNumbers = list(filter(isEven, tempList))
print(evenNumbers)