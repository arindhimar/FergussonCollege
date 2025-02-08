#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int sum =1;
    for(int i=2;i<n;i++){
        if(n%i==0)sum+=i;
        
    }
    // cout<<"Sum = "<<sum;
    if(sum == n)cout<<"YES";
    else cout<<"NO";
    return 0;
}