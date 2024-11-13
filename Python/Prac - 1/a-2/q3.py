def sum(*args):
    # print(args[0])
    total = 0
    for temp in args:
        total+=temp
    print("Total : "+str(total))


sum(*[1,2,3,4,5])