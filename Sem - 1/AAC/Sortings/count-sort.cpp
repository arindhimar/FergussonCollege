#include <bits/stdc++.h>
using namespace std;

void countSort(vector<int> &arr, int n)
{
    int max_ele = *max_element(arr.begin(), arr.end());
    vector<int> countArray(max_ele + 1, 0);

    for (int i = 0; i < n; i++)
    {
        countArray[arr[i]]++;
    }

    for (int i = 1; i <= max_ele; i++)
    {
        countArray[i] += countArray[i - 1];
    }

    vector<int> outputArray(n);

    for (int i = n - 1; i >= 0; i--)
    {
        outputArray[countArray[arr[i]] - 1] = arr[i];
        countArray[arr[i]]--;
    }

    for (int i = 0; i < n; i++)
    {
        cout << outputArray[i] << " ";
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

    countSort(v, n);

    return 0;
}