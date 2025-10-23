#include <bits/stdc++.h>
using namespace std;

int main() {   
    vector<int> v = {3, 5, 8, 9, 15, 19};
    int n = v.size();
    int x = 9;

    for (int i = n - 1; i >= 0; i--) {
        if (v[i] <= x) {
            cout << "Found at " << i;
            return 0;
        }
    }

    cout << "Not found!!";
    return 0;
}
