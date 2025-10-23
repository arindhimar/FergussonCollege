#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={3,4,13,13,13,20,40};

    int n=7,t=13;

    for(int i=n-1;i>=0;i--){
        if(v[i]==t){
            cout<<"Found at "<<i;
            exit(0);
        }
    }

    return 0;
}