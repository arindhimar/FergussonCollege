def sum(*args):
    total = 0
    for i in args:
        total += i
    print("Sum : ", total)

b = True
l = []
while b:
    data = eval(input("Enter number: "))
    if isinstance(data, (int, float)):
        l.append(data)
    b = input("Enter False to exit: ").lower() != 'false'

sum(*l)