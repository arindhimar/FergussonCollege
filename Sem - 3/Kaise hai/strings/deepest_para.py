s = "(1+(2*3)+((8)/4))+1"

count = 0
maxCount = 0
digit = None

for ch in s:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1
    elif ch.isdigit():
        if count > maxCount:
            maxCount = count
            digit = ch

print(digit)
