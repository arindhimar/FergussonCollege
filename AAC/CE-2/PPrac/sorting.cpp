#include <bits/stdc++.h>
using namespace std;

void maxHeap(vector<int> &arr, int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[largest] < arr[left])
        largest = left;
    if (right< n && arr[largest] < arr[right])
        largest = right;

    if (i != largest)
    {
        swap(arr[i], arr[largest]);
        maxHeap(arr, n, largest);
    }
}

void heapSort(vector<int> &arr, int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
    {
        maxHeap(arr, n, i);
    }

    for (int i = n - 1; i >= 0; i--)
    {
        swap(arr[0], arr[i]);
        maxHeap(arr, i, 0);
    }
}

void printArr(vector<int> &arr)
{
    cout << endl;
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    heapSort(arr, n);

    printArr(arr);
    return 0;
}