def multiply(a,*args):
    p = 1
    for temp in args:
        p+=a*temp
    return p


# print(multiply(2,*[1,2,3,4]))


print([1,2,3,4,5,6,7,8,9,0][1::2])