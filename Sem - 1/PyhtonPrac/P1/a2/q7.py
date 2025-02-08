def mult(a, *args):
    result = []
    for temp in args:
        result.append(temp * a)
    return result

print(mult(2, *[1, 2, 3, 4, 5]))