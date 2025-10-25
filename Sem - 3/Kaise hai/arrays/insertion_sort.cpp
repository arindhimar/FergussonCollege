#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v = {1, 2, 4, 2, 3, 1, 4, 5, 1};

    int n = v.size();

    for(int i = 1; i < n; i++) {
        int curr = v[i];
        int j = i - 1;

        cout<<"Iteration";
        for (auto i : v) {
        cout << i << " ";
    }
    cout<<endl;
        while (j >= 0 && v[j] > curr) {
            v[j + 1] = v[j];
            j--;
        }

        v[j + 1] = curr;
    }

    cout << "Sorted!!" << endl;
    for (auto i : v) {
        cout << i << " ";
    }

    return 0;
}
