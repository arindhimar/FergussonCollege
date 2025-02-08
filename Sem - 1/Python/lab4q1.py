from math_operations import advanced_operations,basic_operations

def print_options():
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiply")
    print("4 - Division")
    print("5 - Power")
    print("6 - SquareRoot")
    print("7 - Exit")
    
    



while True:
    print_options()
    opt = int(input("Select Option: "))
    
    if opt == 7:
        chk = input("Enter 'false' to exit: ")
        if chk.lower() == 'false':
            break
    else:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        
        match opt:
            case 1:
                print(basic_operations.addition(a,b))
            case 2:
                print(basic_operations.subtraction(a,b))
            case 3:
                print(basic_operations.multiple(a,b))
            case 4:
                print(basic_operations.divide(a,b))
            case 5:
                print(advanced_operations.power(a,b))
            case 6:
                print(advanced_operations.squareRoot(a))
            case _:
                print("Invalid option")