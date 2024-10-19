#include<bits/stdc++.h>
using namespace std;

void palindromeString(string s){
    int l = 0;
    int r = s.length()-1;
    while (l<=r)
    {
        if (s[l]==s[r])
        {
            l++;
            r--;

        }
        else{
            cout<<"No";
            return;
        }
        
    }

    cout<<"Yes";

    
}



int main()
{
    string s;
    cin>>s;
    palindromeString(s);
    return 0;
}