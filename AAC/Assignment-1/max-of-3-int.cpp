#include<bits/stdc++.h>
using namespace std;

void maxOf3numbers(int a,int b,int c){
    if(a>=b&&b>=c){
        cout<<a;
    }
    else if(b>=c&&b>=a){
        cout<<b;
    }
    else if(c>=a&&c>=b){
        cout<<c;
    }
    else{
        cout<<a;
    }
}

int main()
{
    int a,b,c;
    cin>>a>>b>>c;
    maxOf3numbers(a,b,c);
    return 0;
}