#include<bits/stdc++.h>
using namespace std;

void fact(int n){
    int fact = 1;
    for(int i=2;i<=n;i++){
        fact*=i;
    }
    cout<<"Fact : "<<fact<<endl;
}

int rec_fact(int n){
    if(n==1) return 1;
    return n*rec_fact(n-1);
}

int main()
{
    int n;
    cin>>n;

    fact(n);
    cout<<"Fact : "<<rec_fact(n);
    return 0;
}