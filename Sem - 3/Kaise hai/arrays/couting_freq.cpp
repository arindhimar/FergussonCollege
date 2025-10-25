#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> v = {1, 2, 4, 2, 3, 1, 4, 5, 1};
    

    

    unordered_map<int,int> um;

    for(auto i:v){
        um[i]++;
    }

    for(auto u:um){
        cout<<u.first<< "-"<<u.second<<endl;
    }

    int maxe=-1;
    int mine=-1;
    int minCount=INT_MAX;
    int maxCount=INT_MIN;

    for(auto u:um){
        if(u.second>maxCount){
            maxCount=u.second;
            maxe=u.first;
        }
    }

    for(auto u:um){
        if(u.second<minCount){
            minCount=u.second;
            mine=u.first;
        }
    }

    cout<<"Min : "<<mine<< ", Max : "<<maxe;
    

    return 0;
}