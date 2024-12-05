def arrSum(*args):
    sum=0
    for temp in args:
        sum+=temp
    print(sum)
        

arrSum(*[1,2,3,4,5])