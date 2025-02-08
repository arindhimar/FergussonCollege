#include<bits/stdc++.h>
using namespace std;

void bubbleSort(vector<int> &a,int n){
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n-1;j++){
            if(a[j]>a[j+1]){
                swap(a[j],a[j+1]);
            }
        }
    }
}

int main()
{
    int n;
    cin>>n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int val ;
        cin>>val;
        v.push_back(val);
    }

    bubbleSort(v,n);

    for(int i=0;i<n;i++){
        cout<<v[i]<<" ";
    }
    return 0;
}