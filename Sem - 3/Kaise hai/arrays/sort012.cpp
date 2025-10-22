#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v = {2,0,2,1,1,0};

    int n = v.size();

    unordered_map<int, int> um;


    for(auto i:v){
        um[i]++;
    }
    int l=0;
    for(int i=0;i<um[0];i++){
        v[l++]=0;
    }
    for(int i=0;i<um[1];i++){
        v[l++]=1;
    }
    for(int i=0;i<um[2];i++){
        v[l++]=2;
    }
    cout<<endl;
    for(auto i : v){
        cout<<i;
    }

    return 0;
}