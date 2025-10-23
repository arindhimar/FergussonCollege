#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={3, 4, 4, 7, 8, 10};
    int n = 6,x=8;


    for(int i=0;i<n;i++){
        if(v[i]>=x){
            cout<<"Upper at"<<i;
            break;
        }
    }

    for(int i=n-1;i>=0;i--){
        if(v[i]<=x){
            cout<<"Lowet at"<<i;
            break;

        }
    }

    return 0;
}