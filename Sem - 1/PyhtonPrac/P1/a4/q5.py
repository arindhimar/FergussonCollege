pow = lambda x, y: x ** y

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = list(map(pow, list1, list2))

print(result)