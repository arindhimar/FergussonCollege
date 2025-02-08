def multiply(a,*args):
    for i in args:    
        print(i*a)
    

b = True
l = []
while b:
    data = eval(input("Enter number: "))
    if isinstance(data, (int, float)):
        l.append(data)
    b = input("Enter False to exit: ").lower() != 'false'

a = eval(input("Enter number"))

multiply(a,*l)