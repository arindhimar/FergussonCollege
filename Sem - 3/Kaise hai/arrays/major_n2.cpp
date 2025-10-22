#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v = {2,2,1,1,1,2,2};
    int n = 7;

    int k=n/2;
    unordered_map<int,int> um;


    for(int i=0;i<n;i++)
    {
        um[v[i]]++;
    }


    cout<<"Below:";
    for (auto p : um) {
        cout << p.first << " - " << p.second << endl;
        if (p.second > k) {
            cout << "=> Majority Element is: " << p.first << endl;
        }
    }

    return 0;
}