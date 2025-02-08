def square(a):
    return a * a

result = map(square, [1, 2, 3, 4])

result_list = list(result)

print(result_list)

for result in map(square, [1, 2, 3, 4]):
    print(result)