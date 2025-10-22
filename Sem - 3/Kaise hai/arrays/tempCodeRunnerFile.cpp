#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={1,2,3,4,5,1};


    int n=v.size();
    for(int i=1;i<n;i++){
        if(v[i]==v[i-1]){
            cout<<"Found";
            // return 0;
        }
    }

    cout<<"sorted!";

    return 0;
}