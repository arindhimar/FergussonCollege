#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={10, 22, 12, 3, 0, 6};

    int n = v.size();

    int max = v[n - 1];
    cout<<max;
    for(int i=n-2;i>=0;i--){
        if(v[i]>max){
            cout<<v[i];
            max=v[i];
        }
    }




    return 0;
}