def multiply(a,*args):
    prod = 0
    for data in args:
        prod+=a*data
    print("Product : "+str(prod))
    
multiply(5,*[1,2,3,4,5])