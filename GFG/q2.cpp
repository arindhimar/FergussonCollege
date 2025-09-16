#include<bits/stdc++.h>
using namespace std;
int main()
{
    unordered_set<int>us;
    us.insert(10);
    us.insert(20);
    us.insert(10);

    for(auto x:us)
    {
        cout<<x<<endl;
    }

    return 0;
}
