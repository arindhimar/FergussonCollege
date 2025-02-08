#include<bits/stdc++.h>
using namespace std;


void linearSearch(vector<int>& arr,int n){
    int temp;
    cin>>temp;

    for(int i=0;i<n;i++){
        if(arr[i]==temp){
            cout<<"index: "<<i<<endl;
            break;
        }
    }
    cout<<"element found!";
}

int main()
{
    int n;
    cin>>n;
    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }

    linearSearch(arr,n);
    

    return 0;
}