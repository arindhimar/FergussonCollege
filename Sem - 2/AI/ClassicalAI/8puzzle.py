# Goal state of the 8-puzzle
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]  # 0 is the empty tile

# Heuristic: Manhattan distance (simplified and readable)
def h(state):
    total = 0
    for i, val in enumerate(state):
        if val != 0:
            # Current position
            cur_row, cur_col = i // 3, i % 3

            # Goal position for this tile
            goal_row, goal_col = (val - 1) // 3, (val - 1) % 3

            # Add distance to total
            total += abs(cur_row - goal_row) + abs(cur_col - goal_col)
    return total

# Get all valid neighbor states by sliding the empty tile
def neighbors(state):
    i = state.index(0)  # Index of the empty tile
    moves = []
    for d in [-3, 3, -1, 1]:  # Up, Down, Left, Right moves
        ni = i + d
        # Check for valid index and no row wrapping
        if 0 <= ni < 9 and not (i % 3 == 0 and d == -1) and not (i % 3 == 2 and d == 1):
            new = state[:]  # Copy the current state
            new[i], new[ni] = new[ni], new[i]  # Swap the tiles
            moves.append(new)
    return moves

# Optional: Print the puzzle as a 3x3 grid
def print_grid(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Hill Climbing algorithm
def hill_climb(start):
    cur = start
    step = 0
    while True:
        print(f"Step {step} (h={h(cur)}):")
        print_grid(cur)

        if h(cur) == 0:
            print("🎯 Goal reached!")
            break

        nexts = neighbors(cur)
        better = min(nexts, key=h)

        if h(better) >= h(cur):
            print("⚠️ No better neighbor found. Stopping.")
            break

        cur = better
        step += 1

# 🔧 Try with this starting state (you can change it)
start_state = [1, 2, 3,
               4, 0, 6,
               7, 5, 8]

hill_climb(start_state)

# heuristic = how far a tile is from its goal position, by only counting horizontal and vertical moves