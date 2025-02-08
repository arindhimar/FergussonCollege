#include<bits/stdc++.h>
using namespace std;

void fibonacciSeries(int n){
    int a=0,b=1,c=0;
    cout<<a<<" "<<b<<" ";
    for(int i=0;i<=n;i++){
        c=a+b;
        cout<<c<<" ";
        a=b;
        b=c;
    }
}

int main()
{
    int n;
    cin>>n;
    fibonacciSeries(n);
    return 0;
}