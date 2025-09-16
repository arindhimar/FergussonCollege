#include<bits/stdc++.h>
using namespace std;

int binary_search(vector<int>&v,int key)
{
    int low=0;
    int high=v.size()-1;

    while(low<=high)
    {
        int mid=(low+high)/2;
        if(v[mid]==key)
        {
            return mid;
        }
        else if(v[mid]<key)
        {
            low=mid+1;
        }
        else
        {
            high=mid-1;
        }
    }
    return -1;
}

int main()
{
    vector<int>v;
    v.push_back(50);
    v.push_back(10);
    v.push_back(20);
    v.push_back(40);
    v.push_back(30);

    sort(v.begin(),v.end());

    
    if(binary_search(v.begin(),v.end(),30))
    {
        cout<<"Found"<<endl;
    }
    else
    {
        cout<<"Not Found"<<endl;
    }
    return 0;
}