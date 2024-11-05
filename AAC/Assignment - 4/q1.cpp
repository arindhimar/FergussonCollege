#include <iostream>
#include <vector>
#include <stack>

using namespace std;

const int MAX_VERTICES = 100; // Maximum number of vertices
vector<int> adj[MAX_VERTICES]; // Adjacency list
bool visited[MAX_VERTICES]; // Visited array
stack<int> Stack; // Stack to store the topological order

// Function to add an edge to the graph
void addEdge(int u, int v) {
    adj[u].push_back(v);
}

// A recursive function to perform DFS and store the topological sort
void topologicalSortUtil(int v) {
    visited[v] = true;

    // Recur for all the vertices adjacent to this vertex
    for (int i : adj[v]) {
        if (!visited[i]) {
            topologicalSortUtil(i);
        }
    }

    // Push current vertex to stack which stores the result
    Stack.push(v);
}

// Function to perform topological sort
void topologicalSort(int V) {
    // Initialize all vertices as not visited
    fill(visited, visited + V, false);

    // Call the recursive helper function to store the topological sort
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topologicalSortUtil(i);
        }
    }

    // Print the contents of stack
    cout << "Topological Sort: ";
    while (!Stack.empty()) {
        cout << Stack.top() << " ";
        Stack.pop();
    }
    cout << endl;
}

int main() {
    int V, E;
    cout << "Enter number of vertices: ";
    cin >> V;
    cout << "Enter number of edges: ";
    cin >> E;

    cout << "Enter the edges (u v) where u -> v:" << endl;
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        addEdge(u, v);
    }

    topologicalSort(V);

    return 0;
}


/*
Enter number of vertices: 6
Enter number of edges: 6
Enter the edges (u v) where u -> v:
5 2
5 0
4 0
4 1
2 3
3 1
*/