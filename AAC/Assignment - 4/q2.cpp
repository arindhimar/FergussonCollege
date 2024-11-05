#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Graph {
    int V;  // Number of vertices
    vector<pair<int, pair<int, int> > > edges;  // Edges for Kruskal's algorithm
    vector<pair<int, int> >* adj;  // Adjacency list for Prim's algorithm

public:
    Graph(int V) {
        this->V = V;
        adj = new vector<pair<int, int> >[V];
    }

    void addEdge(int u, int v, int weight) {
        adj[u].push_back(make_pair(v, weight));
        adj[v].push_back(make_pair(u, weight));
        edges.push_back(make_pair(weight, make_pair(u, v)));  // For Kruskal's
    }

    void primsMST() {
        int *key = new int[V];           // Minimum edge weight to reach each vertex
        int *parent = new int[V];        // Stores MST edges
        bool *inMST = new bool[V];       // MST inclusion

        for (int i = 0; i < V; i++) {
            key[i] = INT_MAX;
            inMST[i] = false;
        }

        key[0] = 0;
        parent[0] = -1;

        for (int count = 0; count < V - 1; count++) {
            int u = -1;

            // Find the vertex with minimum key value that's not yet in MST
            for (int v = 0; v < V; v++) {
                if (!inMST[v] && (u == -1 || key[v] < key[u])) {
                    u = v;
                }
            }

            inMST[u] = true;

            // Update key and parent for adjacent vertices
            for (size_t i = 0; i < adj[u].size(); i++) {
                int v = adj[u][i].first;
                int weight = adj[u][i].second;

                if (!inMST[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                }
            }
        }

        cout << "Prim's MST:\n";
        for (int i = 1; i < V; i++) {
            cout << parent[i] << " - " << i << " \t" << key[i] << endl;
        }

        delete[] key;
        delete[] parent;
        delete[] inMST;
    }

    int find(int u, int parent[]) {
        if (u != parent[u])
            parent[u] = find(parent[u], parent);
        return parent[u];
    }

    void unionSet(int u, int v, int parent[], int rank[]) {
        int rootU = find(u, parent);
        int rootV = find(v, parent);

        if (rank[rootU] < rank[rootV]) {
            parent[rootU] = rootV;
        } else if (rank[rootU] > rank[rootV]) {
            parent[rootV] = rootU;
        } else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
    }

    void kruskalsMST() {
        sort(edges.begin(), edges.end());

        int *parent = new int[V];
        int *rank = new int[V];

        for (int i = 0; i < V; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        cout << "Kruskal's MST:\n";
        for (size_t i = 0; i < edges.size(); i++) {
            int weight = edges[i].first;
            int u = edges[i].second.first;
            int v = edges[i].second.second;

            int setU = find(u, parent);
            int setV = find(v, parent);

            if (setU != setV) {
                cout << u << " - " << v << " \t" << weight << endl;
                unionSet(setU, setV, parent, rank);
            }
        }

        delete[] parent;
        delete[] rank;
    }
};

int main() {
    int V = 5;
    Graph g(V);

    g.addEdge(0, 1, 2);
    g.addEdge(0, 3, 6);
    g.addEdge(1, 3, 8);
    g.addEdge(1, 4, 5);
    g.addEdge(1, 2, 3);
    g.addEdge(2, 4, 7);

    g.primsMST();
    cout << endl;
    g.kruskalsMST();

    return 0;
}
