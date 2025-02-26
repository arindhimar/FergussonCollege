#include<bits/stdc++.h>
using namespace std;
int main()
{
    //next lexographical permutation wihout using stl function

    vector<int> arr;

    int n;

    cin>>n;
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        arr.push_back(x);
    }

    // next_permutation(arr.begin(),arr.end());

    int i = n-2;
    while(i>=0 && arr[i]>=arr[i+1])
    {
        i--;
    }

    if(i>=0)
    {
        int j = n-1;
        while(j>=0 && arr[j]<=arr[i])
        {
            j--;
        }
        swap(arr[i],arr[j]);
    }

    reverse(arr.begin()+i+1,arr.end());

    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

    


    return 0;
}