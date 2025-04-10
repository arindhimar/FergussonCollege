import heapq

def tsp_a_star(graph, start, end):
    n = len(graph)
    heap = [(0, start, [start], set([start]))]

    while heap:
        cost, city, path, visited = heapq.heappop(heap)

        if len(visited) == n and city == end:
            return path, cost

        for next_city in range(n):
            if next_city not in visited or (len(visited) == n-1 and next_city == end):
                new_visited = visited | {next_city}
                g = cost + graph[city][next_city]

                # Safe heuristic: 0 if no cities left, else min of remaining
                unvisited = [k for k in range(n) if k not in new_visited and k != end]
                h = min((graph[next_city][k] for k in unvisited), default=0)

                heapq.heappush(heap, (g + h, next_city, path + [next_city], new_visited))

# Example graph
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

start = int(input("Enter starting city (0 to 3): "))
end = int(input("Enter ending city (0 to 3): "))

path, cost = tsp_a_star(graph, start, end)
print("🛣️ Path:", path)
print("💰 Total Cost:", cost)
