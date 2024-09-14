def max_value(a,b,c):
    if a == b ==c:
        return a
    elif a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    


a=int(input("Enter number 1     "))
b=int(input("Enter number 2     "))
c=int(input("Enter number 3     "))
print(max_value(a,b,c))
