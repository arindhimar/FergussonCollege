#include<bits/stdc++.h>
using namespace std;

void perfect_number(int n){
    int sum = 1;
    for(int i=2;i<n;i++)
    {
        if(n%i==0){
            sum+=i;
        }
    }

    if(sum==n){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
}

int main()
{
    int n;
    cin>>n;

    perfect_number(n);

    return 0;
}