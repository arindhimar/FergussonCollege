#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<string>v;
    v.push_back("apple");
    v.push_back("banana");

    for(auto x:v)
    {
        cout<<x<<endl;
    }

    if(find(v.begin(),v.end(),"apple")!=v.end())
    {
        cout<<"Found"<<endl;
    }
    else
    {
        cout<<"Not Found"<<endl;
    }

    return 0;
}