tempPower = lambda a, b: a ** b

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

result = list(map(tempPower, l1, l2))
print(result)