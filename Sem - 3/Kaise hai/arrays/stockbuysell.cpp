#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v = {7,6,4,3,1};

    int n=v.size();
    int maxProfit=INT_MIN;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int profit = v[j]-v[i];
            maxProfit = max(maxProfit,profit);
        }
    }

    cout<<"Profit : "<<maxProfit;

    return 0;
}