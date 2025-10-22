#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n = 5, k = 10;
    
    vector<int> v= {2,3,5,1,9};


    for(int i=0;i<n;i++){
        // int count=0;
        for(int j=i+1;j<n;j++){
        int sum = v[i];
            
            sum+=v[j];
            if(sum==k){
                // cout<<"HI";
                cout<<" i : "<<i<<" j : "<<j;
            }
        }
    }

    // cout<<"Lol : "<<maxLen;
    return 0;
}