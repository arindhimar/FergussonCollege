#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int knapsack(int W, const vector<int>& weights, const vector<int>& values, int n) {
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][W];
}

int main() {
    int W;
    int n;

    cout << "Enter the capacity of the knapsack: ";
    cin >> W;

    cout << "Enter the number of items: ";
    cin >> n;

    vector<int> weights(n);
    vector<int> values(n);

    cout << "Enter the weights of the items:\n";
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }

    cout << "Enter the values of the items:\n";
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    int maxValue = knapsack(W, weights, values, n);
    cout << "Maximum value in the knapsack: " << maxValue << endl;

    return 0;
}