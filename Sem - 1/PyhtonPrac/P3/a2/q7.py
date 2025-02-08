def multiply(a, *args):
    product = 1
    for temp in args:
        print(temp*a)
    
    
    
num = [1,2,3,4]

multiply(2,*num)