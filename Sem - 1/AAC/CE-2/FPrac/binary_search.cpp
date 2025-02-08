#include<bits/stdc++.h>
using namespace std;

void linear_search(){
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int temp;
    cin>>temp;

    sort(arr.begin(),arr.end());

    int low = 0;
    int high = n-1;
    

    while(low<=high){
        int mid = (low+high)/2;
        if(arr[mid]==temp){
            cout<<mid;
            return;
        }

        if(arr[mid]<temp){
            low = mid+1;
        }
        else{
            high = mid-1;
        }

    }

    cout<<"NO";
}

int main()
{
    linear_search();
    return 0;
}