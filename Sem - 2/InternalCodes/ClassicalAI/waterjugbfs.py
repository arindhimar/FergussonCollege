from collections import deque

def bfs_water_jug_easy():
    max_a = 5  # Capacity of Jug A (5 liters)
    max_b = 4  # Capacity of Jug B (4 liters)
    goal = 2   # Our goal is to get exactly 2 liters in Jug A

    queue = deque()     # Queue to store states for BFS
    visited = set()     # Set to store already visited states

    # Start with both jugs empty (0, 0)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()  # Get the next state from the queue
        print(f"Checking state: JugA={a}L, JugB={b}L")

        # Check if we've reached our goal
        if a == goal:
            print(f"\n🎯 Found solution: JugA has {a}L")
            return

        # Generate all possible next valid states from current state
        possible_moves = [

            # 1. Fill Jug A completely
            (max_a, b),

            # 2. Fill Jug B completely
            (a, max_b),

            # 3. Empty Jug A
            (0, b),

            # 4. Empty Jug B
            (a, 0),

            # 5. Pour water from Jug A to Jug B
            # Only pour as much as Jug B can take
            (a - min(a, max_b - b), b + min(a, max_b - b)),

            # 6. Pour water from Jug B to Jug A
            # Only pour as much as Jug A can take
            (a + min(b, max_a - a), b - min(b, max_a - a))
        ]

        # Add each new state to the queue if not already visited
        for move in possible_moves:
            if move not in visited:
                visited.add(move)
                queue.append(move)

    # If we exhaust the queue without finding the goal
    print("❌ No solution found.")

# Run the function
bfs_water_jug_easy()
