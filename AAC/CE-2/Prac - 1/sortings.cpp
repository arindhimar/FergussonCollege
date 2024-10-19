#include <bits/stdc++.h>
using namespace std;

void insertionSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];

        int j = i - 1;

        while (j >= 0 && key < arr[j])
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

void selectionSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
    {
        int mix_idx = i;

        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[mix_idx])
                mix_idx = j;
        }

        if (mix_idx != i)
            swap(arr[mix_idx], arr[i]);
    }
}

void bubbleSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void mergeSort(vector<int> &arr, int low, int mid, int high)
{
    vector<int> temp;

    int left = low;
    int right = mid + 1;

    while (left <= mid && right <= high)
    {
        if (arr[left] < arr[right])
        {
            temp.push_back(arr[left]);
            left++;
        }
        else
        {
            temp.push_back(arr[right]);
            right++;
        }
    }

    while (left <= mid)
    {
        temp.push_back(arr[left]);
        left++;
    }
    while (right <= high)
    {
        temp.push_back(arr[right]);
        right++;
    }

    for (int i = 0; i < temp.size(); i++)
    {
        arr[low + i] = temp[i];
    }
}

void mergePartition(vector<int> &arr, int low, int high)
{
    if (low >= high)
        return;

    int mid = (low + high) / 2;

    mergePartition(arr, low, mid);
    mergePartition(arr, mid + 1, high);

    mergeSort(arr, low, mid, high);
}

int quickSort(vector<int> &arr, int low, int high)
{
    // cout<<"Here";
    int i = low+1;
    int j = high;
    int pivot = arr[low];

    while (i <= j)
    {
        while (i <= high && arr[i] <= pivot)
            i++;
        while (j >= low && arr[j] > pivot)
            j--;

        if(i<j) swap(arr[i],arr[j]);


    }

    swap(arr[j],arr[low]);

    return j;
}

void quickPartition(vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int p = quickSort(arr, low, high);
        quickPartition(arr, low, p-1);
        quickPartition(arr, p + 1, high);
    }
}

void printArray(vector<int> &arr)
{
    cout << endl;
    int n = arr.size();

    cout << "Sorted Array : ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}
void countSort(vector<int>& arr) {
    // if (size <= 0) return;
    int size = arr.size();
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    int* countsArr = new int[max + 1]();
    for (int i = 0; i < size; i++) {
        countsArr[arr[i]]++;
    }

    for (int i = 1; i <= max; i++) {
        countsArr[i] += countsArr[i - 1];
    }

    int* newArr = new int[size];
    for (int i = size - 1; i >= 0; i--) {
        newArr[countsArr[arr[i]] - 1] = arr[i];
        countsArr[arr[i]]--;
    }

    for (int i = 0; i < size; i++) {
        arr[i] = newArr[i];
    }

}

int main()
{
    vector<int> arr;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    // bubbleSort(arr);
    // insertionSort(arr);
    // selectionSort(arr);
    // mergePartition(arr, 0, n);
    // quickPartition(arr,0,n);

    countSort(arr);

    printArray(arr);

    return 0;
}