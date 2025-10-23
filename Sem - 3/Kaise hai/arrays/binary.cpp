#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={3, 4, 6, 7, 9, 12, 16, 17};
    int n=v.size();
    int t=6;
    int l=0,r=n-1;

    while(l<=r){
        int m=(l+r)/2;
        if(v[m]==t){
            cout<<"Found at "<<m;
            return 0;
        }
        else if(v[m]>t){
            r=m-1;
        }
        else{
            l=m+1;
        }
    }
    cout<<"Not found!!";

    return 0;
}