#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={1,2,3,4,5};


    int n=v.size();
    
    int d = 3;

    int nd = d%n;

    vector<int> f;

    f.insert(f.end(), v.begin() + nd, v.end());
    f.insert(f.end(), v.begin(), v.begin() + nd);



    cout<<"LOL"<<endl;
    for (auto i : f) {
        cout << i;
    }

    return 0;
}