#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> arr;

    int n;

    cin>>n;

    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        arr.push_back(x);
    }

    int prod = 1;

    for(int i=0;i<n;i++)
    {
        prod *= arr[i];
    }

    for(int i=0;i<n;i++)
    {
        cout<<prod/arr[i]<<" ";
    }

    return 0;
}