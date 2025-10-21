#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v = {1, 2, 4, 2, 3, 1, 4, 5, 1};

    int n = v.size();
    for(int i=0;i<n;i++){
        int min_ele = i;

        for(int j=i+1;j<n;j++){
            if(v[j]<v[min_ele]){
                min_ele = j;
            }
        }

        swap(v[i],v[min_ele]);
    }

    cout<<"Sorted!!"<<endl;
    for(auto i:v){
        cout<<i;
    }

    return 0;
}