#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <utility>

using namespace std;

void dijkstra(int source, const vector<vector<pair<int, int> > >& graph, vector<int>& distances) {
    // Define the priority queue
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
    distances[source] = 0;
    pq.push(make_pair(0, source));

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        // Process each neighbor of u
        for (size_t i = 0; i < graph[u].size(); i++) {
            int v = graph[u][i].first;
            int weight = graph[u][i].second;

            // Check if a shorter path to v is found
            if (distances[u] + weight < distances[v]) {
                distances[v] = distances[u] + weight;
                pq.push(make_pair(distances[v], v));
            }
        }
    }
}

int main() {
    int V = 9;
    vector<vector<pair<int, int> > > graph(V);

    // Add edges
    graph[0].push_back(make_pair(1, 4));
    graph[0].push_back(make_pair(7, 8));
    graph[1].push_back(make_pair(0, 4));
    graph[1].push_back(make_pair(2, 8));
    graph[1].push_back(make_pair(7, 11));
    graph[2].push_back(make_pair(1, 8));
    graph[2].push_back(make_pair(3, 7));
    graph[2].push_back(make_pair(5, 4));
    graph[2].push_back(make_pair(8, 2));
    graph[3].push_back(make_pair(2, 7));
    graph[3].push_back(make_pair(4, 9));
    graph[3].push_back(make_pair(5, 14));
    graph[4].push_back(make_pair(3, 9));
    graph[4].push_back(make_pair(5, 10));
    graph[5].push_back(make_pair(2, 4));
    graph[5].push_back(make_pair(3, 14));
    graph[5].push_back(make_pair(6, 2));
    graph[6].push_back(make_pair(5, 2));
    graph[6].push_back(make_pair(7, 1));
    graph[6].push_back(make_pair(8, 6));
    graph[7].push_back(make_pair(0, 8));
    graph[7].push_back(make_pair(1, 11));
    graph[7].push_back(make_pair(6, 1));
    graph[7].push_back(make_pair(8, 7));
    graph[8].push_back(make_pair(2, 2));
    graph[8].push_back(make_pair(6, 6));
    graph[8].push_back(make_pair(7, 7));

    // Initialize distances vector
    vector<int> distances(V, INT_MAX);
    dijkstra(0, graph, distances);

    // Print the result
    cout << "Vertex Distance from Source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << "\t\t" << distances[i] << endl;
    }

    return 0;
}
