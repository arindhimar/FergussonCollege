#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 1, 2, 3, 4, 5};

    int n = v.size();
    for (int i = 1; i < v.size(); i++) {
        if (v[i] == v[i - 1]) {
            v.erase(v.begin() + i);
            i--;  
        }
    }

    for (auto i : v) {
        cout << i;
    }

    return 0;
}
