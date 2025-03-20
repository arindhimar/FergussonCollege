import java.util.*;

class Node {
    String name;
    int cost;

    public Node(String name, int cost) {
        this.name = name;
        this.cost = cost;
    }
}

class Graph {
    private final Map<String, List<Node>> adjList = new HashMap<>();
    private final Map<String, Integer> heuristic = new HashMap<>();

    // Add an edge to the graph (Bidirectional)
    public void addEdge(String src, String dest, int cost) {
        adjList.putIfAbsent(src, new ArrayList<>());
        adjList.putIfAbsent(dest, new ArrayList<>());
        adjList.get(src).add(new Node(dest, cost));
        adjList.get(dest).add(new Node(src, cost)); // Undirected graph
    }

    // Set heuristic values for nodes
    public void setHeuristic(String node, int hValue) {
        heuristic.put(node, hValue);
    }

    // Check if a node exists in the graph
    public boolean hasNode(String node) {
        return adjList.containsKey(node);
    }

    // Display the graph structure
    public void displayGraph() {
        System.out.println("\n📌 **Graph Representation:**");
        for (var entry : adjList.entrySet()) {
            System.out.print(entry.getKey() + " -> ");
            for (Node neighbor : entry.getValue()) {
                System.out.print(neighbor.name + "(" + neighbor.cost + ")  ");
            }
            System.out.println();
        }
    }

    // Best First Search Algorithm (Greedy BFS)
    public void bestFirstSearch(String start, String goal) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(n -> heuristic.getOrDefault(n.name, Integer.MAX_VALUE)));
        Set<String> visited = new HashSet<>();
        Map<String, String> parent = new HashMap<>();
        Map<String, Integer> pathCost = new HashMap<>(); // Stores cost to reach each node

        pq.add(new Node(start, 0));
        visited.add(start);
        pathCost.put(start, 0);

        System.out.println("\n🔍 **Steps of Best First Search (Greedy BFS):**");
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int currentCost = pathCost.getOrDefault(current.name, 0);

            System.out.println("➡ Exploring: " + current.name + " (Current Cost: " + currentCost + ")");

            if (current.name.equals(goal)) {
                System.out.println("\n✅ **Goal Reached! Shortest Path Found.**");
                printPath(parent, start, goal, pathCost);
                return;
            }

            for (Node neighbor : adjList.getOrDefault(current.name, new ArrayList<>())) {
                if (!visited.contains(neighbor.name)) {
                    visited.add(neighbor.name);
                    pq.add(new Node(neighbor.name, heuristic.getOrDefault(neighbor.name, Integer.MAX_VALUE)));
                    parent.put(neighbor.name, current.name);
                    pathCost.put(neighbor.name, currentCost + neighbor.cost); // Update cost

                    System.out.println("   🔹 Adding to queue: " + neighbor.name + " (Edge Weight: " + neighbor.cost + ", Total Cost: " + pathCost.get(neighbor.name) + ")");
                }
            }
        }
        System.out.println("\n⚠️ No path found between " + start + " and " + goal);
    }

    // Print the shortest path
    private void printPath(Map<String, String> parent, String start, String goal, Map<String, Integer> pathCost) {
        List<String> path = new ArrayList<>();
        String current = goal;
        int totalCost = pathCost.get(goal);

        while (current != null) {
            path.add(current);
            current = parent.get(current);
        }
        Collections.reverse(path);
        System.out.println("\n🚀 **Shortest Path:** " + String.join(" -> ", path) + " (Total Cost: " + totalCost + ")");
    }
}

public class BestFirstSearchGraph {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Graph graph = new Graph();

        // Define graph edges
        graph.addEdge("A", "B", 4);
        graph.addEdge("A", "C", 3);
        graph.addEdge("B", "D", 2);
        graph.addEdge("C", "E", 5);
        graph.addEdge("D", "F", 3);
        graph.addEdge("E", "F", 2);
        graph.addEdge("B", "E", 6);
        graph.addEdge("D", "G", 4);
        graph.addEdge("F", "G", 1);

        // Set heuristic values
        graph.setHeuristic("A", 6);
        graph.setHeuristic("B", 4);
        graph.setHeuristic("C", 5);
        graph.setHeuristic("D", 2);
        graph.setHeuristic("E", 3);
        graph.setHeuristic("F", 1);
        graph.setHeuristic("G", 0); // Goal Node

        // Display the graph
        graph.displayGraph();

        // Ask user for start and goal nodes
        System.out.print("\n🌍 Enter Start Node: ");
        String start = scanner.next().toUpperCase();
        System.out.print("🎯 Enter Goal Node: ");
        String goal = scanner.next().toUpperCase();

        // Validate user input
        if (!graph.hasNode(start) || !graph.hasNode(goal)) {
            System.out.println("⚠️ Invalid nodes! Please enter valid nodes from the graph.");
        } else {
            graph.bestFirstSearch(start, goal);
        }

        scanner.close();
    }
}
