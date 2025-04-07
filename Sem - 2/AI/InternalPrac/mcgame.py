def is_valid(m_left, c_left, m_right, c_right):
    # Reject negative numbers
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    # Check missionary safety on the left
    if m_left > 0 and m_left < c_left:
        return False

    # Check missionary safety on the right
    if m_right > 0 and m_right < c_right:
        return False

    return True

def menu_missionaries():
    left = [3, 3]   # [missionaries, cannibals]
    right = [0, 0]
    boat = 'left'

    while True:
        print(f"\n🌊 Boat is on the {boat.upper()} bank")
        print(f"Left -> M: {left[0]} C: {left[1]} | Right -> M: {right[0]} C: {right[1]}")
        
        if right == [3, 3]:
            print("🎉 All safely crossed!")
            break

        try:
            m = int(input("Enter missionaries to move (0-2): "))
            c = int(input("Enter cannibals to move (0-2): "))
        except:
            print("❌ Invalid input")
            continue

        if m + c == 0 or m + c > 2:
            print("⛔ You must move 1 or 2 people.")
            continue

        if boat == 'left':
            if m > left[0] or c > left[1]:
                print("❌ Not enough people on the left.")
                continue
            new_left = [left[0] - m, left[1] - c]
            new_right = [right[0] + m, right[1] + c]
        else:
            if m > right[0] or c > right[1]:
                print("❌ Not enough people on the right.")
                continue
            new_left = [left[0] + m, left[1] + c]
            new_right = [right[0] - m, right[1] - c]

        if not is_valid(*new_left, *new_right):
            print("💀 Missionaries eaten! Invalid move.")
            continue

        # Apply move
        left, right = new_left, new_right
        boat = 'right' if boat == 'left' else 'left'

menu_missionaries()
