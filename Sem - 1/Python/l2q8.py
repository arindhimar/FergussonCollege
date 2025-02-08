l = []
for i in range(10):
    data = eval(input("Enter number: "))
    if isinstance(data, (int, float)):
        l.append(data)
    else:
        l.append(0)
        
print(l[1:10:2])