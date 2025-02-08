a = 10
b = 5

print(a,b)

def myFunction():
    global a
    a=5
    print(a,b)
    
myFunction()

print(a,b)
    