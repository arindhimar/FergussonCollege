fruits = [1, 2, 3, 2, 2]

count = {}
for f in fruits:
    if f in count:
        count[f] += 1
    else:
        count[f] = 1

first_max = second_max = None
first_count = second_count = -1

for key, val in count.items():
    if val > first_count:
        second_count, second_max = first_count, first_max
        first_count, first_max = val, key
    elif val > second_count:
        second_count, second_max = val, key

if first_max is not None and second_max is not None:
    total = first_count + second_count
    print(total)
else:
    print("Not enough distinct elements")
