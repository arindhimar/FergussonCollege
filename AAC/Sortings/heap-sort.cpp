#include <bits/stdc++.h>
using namespace std;

void maxHeapify(vector<int> &arr, int n,int i)
{
    int largest = i;
    int left = 2*i;
    int right = 2*i+1;

    if (left < n && arr[left] < arr[largest]) {
        largest = left;
    }

    if (right < n && arr[right] < arr[largest]) {
        largest = right;
    }


    if(largest!=i){
        swap(arr[largest],arr[i]);
        maxHeapify(arr,n,largest);
    }

}

void heapSort(vector<int> &arr,int n){
    for(int i=n/2;i>=0;i--){
        maxHeapify(arr,n,i);
    }
}

int main()
{
    int n;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        v.push_back(val);
    }

    heapSort(v, n);

    for (int i = 0; i < n; i++)
    {
        cout << v[i] << " ";
    }
    return 0;
}