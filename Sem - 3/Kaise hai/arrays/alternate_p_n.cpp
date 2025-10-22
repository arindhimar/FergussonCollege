#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 2, -3, -1, -2, -3};
    vector<int> pos, neg;

    for (int i = 0; i < v.size(); i++) {
        if (v[i] >= 0)
            pos.push_back(v[i]);
        else
            neg.push_back(v[i]);
    }

    vector<int> res;
    int i = 0, j = 0;

    while (i < pos.size() && j < neg.size()) {
        res.push_back(pos[i++]);
        res.push_back(neg[j++]);
    }

    while (i < pos.size()) {
        res.push_back(pos[i++]);
    }

    while (j < neg.size()) {
        res.push_back(neg[j++]);
    }

    for (auto x : res) {
        cout << x << " ";
    }

    return 0;
}
