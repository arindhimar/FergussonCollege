#include<bits/stdc++.h>
using namespace std;

void palindrome(string s){
    int l =0;
    int r = s.length()-1;

    while(l<=r){
        if(s[l]!=s[r]){
            cout<<"No!";
            return;
        }
        l++;r--;
    }

    cout<<"YES";
}

int main()
{
    string s;
    cin>>s;
    palindrome(s);
    return 0;
}