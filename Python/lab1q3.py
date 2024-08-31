choice = True

while choice:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    
    ch = input("Enter the operator (**,//,+, -, *, /, %): ")
    
    if ch == "+":
        print("num1 + num2 = ", (a+b))
    elif ch == "-":
        print("num1 - num2 = ", (a-b))
    elif ch == "*":
        print("num1 * num2 = ", (a*b))
    elif ch == "**":
        print("num1 * num2 = ", (a**b))
    elif ch == "//":
        print("num1 * num2 = ", (a//b))
    elif ch == "/":
        if b != 0:
            print("num1 / num2 = ", (a/b))
        else:
            print("Error: Division by zero is not allowed")
    elif ch == "%":
        if b != 0:
            print("num1 % num2 = ", (a%b))
        else:
            print("Error: Modulus by zero is not allowed")
    else:
        print("Invalid operator. Please enter either **,//,+, -, *, /, or %")
    
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        choice = False