#include<bits/stdc++.h>
using namespace std;


void fibo(int n){
    if (n == 1){cout<<"0"; return;}
    if (n == 2){cout<<"0 1"; return;}
    int a = 0;
    int b = 1;
    cout<<a<<" "<<b;
    for(int i=2;i<n;i++){
        int c= a+b;
        cout<<" "<<c;
        a = b;
        b = c;
    }
}

int rec_fibo(int n){
    if(n==0) return 0; 
    if(n==1) return 1;

    return rec_fibo(n-1)+rec_fibo(n-2);
}

int main()
{
    int n;
    cin>>n;

    fibo(n);
    cout<<"REcur :"<<rec_fibo(n);
    return 0;
}