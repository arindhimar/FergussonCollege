#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> prices;
    int n;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        prices.push_back(temp);
    }

    if (n == 0) {
        cout << 0 << endl;
        return 0;
    }

    int maxProfit = 0;
    int localMin = prices[0];

    for (int i = 1; i < n; i++) {
        if (prices[i] < localMin) {
            localMin = prices[i];
        } else {
            maxProfit = max(maxProfit, prices[i] - localMin);
        }
    }

    cout << maxProfit << endl;
    return 0;
}