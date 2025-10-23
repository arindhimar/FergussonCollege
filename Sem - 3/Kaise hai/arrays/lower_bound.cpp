#include<bits/stdc++.h>
using namespace std;
int main()
{   
    vector<int> v =  {3,5,8,15,19};
    int n=5,x=9;
    for(int i=0;i<n;i++){
        if(v[i]>x){
            cout<<"Found at "<<i;
            return 0;
        }
    }

    cout<<"Not found!!";
    return 0;
}