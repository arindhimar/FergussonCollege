#include<bits/stdc++.h>
using namespace std;

int fact(int n){
    int fact = 1;
    for(int i=2;i<=n;i++){
        fact*=i;
    }
    return fact;
}

int recur_fact(int n){
    if(n==1) return n;

    return n* fact(n-1);
}

int main()
{
    int n;
    cin>>n;
    // cout<<"Factorial : "<<fact(n);
    cout<<"Factorial : "<<recur_fact(n);

    return 0;
}