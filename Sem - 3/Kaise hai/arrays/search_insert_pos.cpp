#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 2, 4, 7};
    int n = v.size();
    int x = 2;

    if (x < v[0]) {
        cout << "Found at 0";
        return 0;
    }

    for (int i = 0; i < n - 1; i++) {
        if (v[i] < x && v[i + 1] > x) {
            cout << "Found at " << i + 1;
            return 0;
        }
    }

    cout << "Found at " << n; 
    return 0;
}
