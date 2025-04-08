def menu_water_jug(x=5, y=4, goal=2):
    a, b = 0, 0  # Start with both jugs empty

    while True:
        print(f"\nJug A: {a}L / {x}L | Jug B: {b}L / {y}L")
        if a == goal or b == goal:
            print("🎯 Goal Reached!")
            break

        print("""
1. Fill Jug A
2. Fill Jug B
3. Empty Jug A
4. Empty Jug B
5. Pour A -> B
6. Pour B -> A
7. Exit
""")
        choice = input("Choose move: ")

        if choice == '1': a = x
        elif choice == '2': b = y
        elif choice == '3': a = 0
        elif choice == '4': b = 0
        elif choice == '5':
            pour = min(a, y - b)
            a -= pour
            b += pour
        elif choice == '6':
            pour = min(b, x - a)
            b -= pour
            a += pour
        elif choice == '7': break
        else: print("❌ Invalid choice.")

menu_water_jug()
