#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n = 5, k = 10;
    
    vector<int> v= {2,3,5,1,9};

    int maxLen=INT_MIN;

    for(int i=0;i<n;i++){
        int sum = 0;
        int count=0;
        for(int j=i;j<n;j++){
            sum +=v[j];
            count++;
            if(sum==k){
                // cout<<"HI";
                maxLen = max(maxLen,count);
            }
        }
    }

    cout<<"Lol : "<<maxLen;
    return 0;
}