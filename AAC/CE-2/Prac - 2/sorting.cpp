#include <bits/stdc++.h>
using namespace std;

void bubbleSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void selectionSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        int min_idx = i;

        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }

        if (min_idx != i)
            swap(arr[i], arr[min_idx]);
    }
}

void insertionSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 1; i < n; i++)
    {
        int j = i - 1;
        int key = arr[i];

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

void mergeSort(vector<int> &arr, int low, int mid, int high)
{
    // cout<<"Here";
    int l = low;
    int r = mid + 1;
    vector<int> temp;
    while (l <= mid && r <= high)
    {
        if (arr[l] < arr[r])
        {
            temp.push_back(arr[l]);
            l++;
        }
        else
        {
            temp.push_back(arr[r]);
            r++;
        }
    }

    while (l <= mid)
    {
        temp.push_back(arr[l]);
        l++;
    }

    while (r <= high)
    {
        temp.push_back(arr[r]);
        r++;
    }

    for (int i = 0; i < temp.size(); i++)
    {
        arr[i + low] = temp[i];
    }
}

void mergePart(vector<int> &arr, int low, int high)
{
    if (low >= high)
        return;
    int mid = (low + high) / 2;

    mergePart(arr, low, mid);
    mergePart(arr, mid + 1, high);
    mergeSort(arr, low, mid, high);
}

int quickSort(vector<int> &arr, int low, int high)
{
    int p = arr[low];
    int l = low + 1;
    int r = high;

    while (l <= r)
    {
        while (l <= high && arr[l] <= p)
        {
            l++;
        }

        while (r >= low && arr[r] > p)
        {
            r--;
        }

        if (l < r)
            swap(arr[l], arr[r]);
    }

    swap(arr[r], arr[low]);

    return r;
}

void quickPart(vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int pi = quickSort(arr, low, high);
        quickPart(arr, low, pi - 1);
        quickPart(arr, pi + 1, high);
    }
}

void countSort(vector<int> &arr){
    int n = arr.size();
    int max = arr[0];

    for(int i=1;i<n;i++){
        if(max<arr[i]){
            max = arr[i];
        }
    }
    
    vector<int> countArr(max+1,0);
    
    for(int i=0;i<n;i++){
        countArr[arr[i]]++;
    }

    for(int i=1;i<=max;i++){
        countArr[i]+=countArr[i-1];
    }

    vector<int> OA(n);

    for(int i=n-1;i>=0;i--){
        OA[countArr[arr[i]] - 1] = arr[i];
        countArr[arr[i]]--;

    }

    for(int i=0;i<n;i++){
        arr[i]=OA[i];
    }
}

void printArray(vector<int> &arr)
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
    cout << "Enter size       ";
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    // bubbleSort(arr);
    // selectionSort(arr);
    // insertionSort(arr);
    // mergePart(arr,0,n);
    // quickPart(arr, 0, n);
    countSort(arr);

    printArray(arr);

    return 0;
}