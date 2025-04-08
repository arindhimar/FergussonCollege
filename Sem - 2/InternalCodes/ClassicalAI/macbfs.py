from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    # Missionaries can't be outnumbered by cannibals on either side
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def bfs_missionaries_cannibals():
    start = (3, 3, 1)  # (missionaries left, cannibals left, boat on left)
    goal = (0, 0, 0)   # all safely crossed
    
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    
    while queue:
        (m_left, c_left, boat), path = queue.popleft()
        
        # Calculate right side
        m_right = 3 - m_left
        c_right = 3 - c_left
        
        # Check if goal is reached
        if (m_left, c_left, boat) == goal:
            print("✅ Solution found!")
            for step in path:
                print(step)
            return

        # All possible boat moves (1 or 2 people)
        moves = [
            (1, 0), (2, 0),     # 1 or 2 missionaries
            (0, 1), (0, 2),     # 1 or 2 cannibals
            (1, 1)              # 1 missionary + 1 cannibal
        ]

        for m_move, c_move in moves:
            if boat == 1:  # Boat on left
                new_state = (m_left - m_move, c_left - c_move, 0)
            else:          # Boat on right
                new_state = (m_left + m_move, c_left + c_move, 1)

            new_m_left, new_c_left, new_boat = new_state
            new_m_right = 3 - new_m_left
            new_c_right = 3 - new_c_left

            if is_valid(new_m_left, new_c_left, new_m_right, new_c_right) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("❌ No solution found.")

# Run it
bfs_missionaries_cannibals()
