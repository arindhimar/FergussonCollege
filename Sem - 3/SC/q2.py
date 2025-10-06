def menu():
    print("\n1 - Max Min Composition")
    print("2 - Max Product Composition")
    print("3 - Exit\n")

while True:
    a = []
    b = []

    n = int(input("Enter number of elements in fuzzy set A: "))
    for i in range(n):
        ele = float(input(f"Enter element {i+1} of A: "))
        a.append(ele)

    m = int(input("Enter number of elements in fuzzy set B: "))
    for i in range(m):
        ele = float(input(f"Enter element {i+1} of B: "))
        b.append(ele)

    menu()
    opt = int(input("Select option: "))

    if opt == 1:
        result = [[min(a[i], b[j]) for j in range(m)] for i in range(n)]
        print("\nMax-Min Composition Matrix:")
        for row in result:
            print(row)

    elif opt == 2:
        result = [[a[i] * b[j] for j in range(m)] for i in range(n)]
        print("\nMax-Product Composition Matrix:")
        for row in result:
            print(row)

    elif opt == 3:
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again.\n")
