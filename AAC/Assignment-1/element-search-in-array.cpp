#include<bits/stdc++.h>
using namespace std;

void vectorSearch(vector<int> v,int f){
    for(int i=0;i<v.size();i++){
        if(v[i]==f){
            cout<<"Element found at index "<<i;
            return;
        }
    }
    cout<<"Element not found!!";
}

int main()
{
    int n,f;
    cin>>n>>f;
    vector<int> v;
    for(int i=0;i<n;i++){
        int val;
        cin>>val;
        v.push_back(val);
    }

    vectorSearch(v,f);
    return 0;
}