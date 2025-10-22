#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v={2, 3, 5, -2, 7, -4};
    int maxSum=INT_MIN;
    int maxLen=0;
    int n = v.size();

    for(int i=0;i<n;i++){
        int sum=0;
        int len = 0;

        for(int j=i;j<n;j++){
            sum+=v[i];
            int maxS = max(maxSum,sum);
            len++;
            if(maxS>maxSum){
                maxLen = len;
                maxSum=maxS;
            }
        }
    }
    
    return 0;
}