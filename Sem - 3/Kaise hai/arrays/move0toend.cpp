#include<bits/stdc++.h>
using namespace std;
int main()
{

    vector<int> v = {1,2,0,0,2,3,1,2,1};
    int count=0;
    int n = v.size();

    for(int i=0;i<n;i++){
        if(v[i]==0){
            count++;
            v.erase(v.begin()+i);
            i--;
        }
    }

    for(int i=0;i<=count;i++){
        v.push_back(0);
    }

    for (auto i : v) {
        cout << i;
    }
    
    return 0;
}
