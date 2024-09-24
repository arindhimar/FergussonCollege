#include <bits/stdc++.h>
using namespace std;

int partition(vector<int> &arr, int low, int high)
{
    // cout<<low<<high<<"==========";
    int pivot = arr[low];

    int i = low + 1;
    int j = high;

    while (i <= j)
    {
        cout<<"OLD I = "<<i;
        while (i <= high && arr[i] <= pivot){
            i++;
            cout<<" new i="<<i<<endl;
        }

        while (j >= low && arr[j] > pivot)
            j--;

        cout<<"j = "<<j<<endl;
        // cout <<"================="<<i<<"==============="<<j;
        if (i < j){
            // cout<<"Yay!!!!!!";
                    swap(arr[i], arr[j]);
        }
    }
    
    //     cout<<endl;
    // for(auto i:arr){
    //     cout<<i<< " ";
    // }

    cout<<"new wakla"<<i<<j<<"==========";
    

    swap(arr[j], arr[low]);

        for(auto i:arr){
        cout<<i<< " ";
    }


    return j;
}

void quickSort(vector<int> &arr, int low, int high)
{

    if (low < high)
    {
        int pIndex = partition(arr, low, high);

        quickSort(arr, low, pIndex - 1);
        quickSort(arr, pIndex + 1, high);
    }
}

int main()
{
    int n;
    cin >> n;
    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        arr.push_back(val);
    }

    quickSort(arr, 0, n - 1);
    cout<<endl;
    for(auto i:arr){
        cout<<i<< " ";
    }

    return 0;
}
