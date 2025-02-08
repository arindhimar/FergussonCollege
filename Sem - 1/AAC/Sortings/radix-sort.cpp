#include <bits/stdc++.h>
using namespace std;

void countSort(vector<int> &arr, int n, int exp)
{
    int output[n];
    int i, count[10] = { 0 };

    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}


void radixsort(vector<int> &arr, int n)
{
    int max_ele = *max_element(arr.begin(), arr.end());
    for (int exp = 1; max_ele / exp > 0; exp *= 10)
        countSort(arr, n, exp);

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
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

    radixsort(v, n);

    return 0;
}