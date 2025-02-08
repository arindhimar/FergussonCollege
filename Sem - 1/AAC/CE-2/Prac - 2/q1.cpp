#include<bits/stdc++.h>
using namespace std;

void fact(int n){
    int fact =1;
    for(int i=2;i<=n;i++){
        fact*=i;
    }

    cout<<"Factorial : "<<fact<<endl;
}

int recur_fact(int n){
    if(n==1) return n;

    return n*recur_fact(n-1);
}

int main()
{
    cout<<recur_fact(5);
    return 0;
}