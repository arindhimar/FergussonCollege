#include <bits/stdc++.h>
using namespace std;

void bubbleSort(vector<int> &arr)
{
    int n = arr.size();

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (arr[j + 1] < arr[j])
            {
                swap(arr[j + 1], arr[j]);
            }
        }
    }
}

void insertionSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            // cout << "Here";
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

void selectionSort(vector<int> &arr)
{
    int n = arr.size();

    for (int i = 0; i < n; i++)
    {
        int min_idx = arr[i];

        for (int j = i; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
            {
                min_idx = j;
            }
        }

        if (i != min_idx)
        {
            swap(arr[i], arr[min_idx]);
        }
    }
}

void countSort(vector<int> &arr)
{
    int n = arr.size();

    int max = arr[0];

    for (int i = 1; i < n; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
    }

    vector<int> countArr(max, 0);

    for (int i = 0; i < n; i++)
    {
        countArr[arr[i]]++;
    }

    for (int i = 1; i < n; i++)
    {
        arr[i] += arr[i - 1];
    }

    vector<int> OA(n, 0);

    for (int i = 0; i < n; i++)
    {
        OA[countArr[i] - 1] = arr[i];
        countArr[i]--;
    }

    for (int i = 0; i < n; i++)
    {
        arr[i] = OA[i];
    }
}

void mergeSort(vector<int> &arr, int low, int mid, int high)
{
    int left = low;
    int right = mid + 1;
    vector<int> temp;
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

    for(int i=0;i<temp.size();i++){
        arr[low+i] = temp[i];
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

int countSort(vector<int> &arr,int low,int high){
    int i = low;
    int j = high;
    int pivot = arr[low];

    while(i<j){
        while(i<=high && arr[i]<=pivot){
            i++;
        }

        while(j>=0&&arr[j]>pivot){
            j--;
        }

        if(i<j){
            swap(arr[i],arr[j]);
        }
    }

    swap(arr[j],arr[low]);

    return j;
}

void countPart(vector<int> &arr,int low,int high){
    if(low<high){
        int p = countSort(arr,low,high);
        countPart(arr,low,p-1);
        countPart(arr,p+1,high);

    }
}

void printArr(vector<int> &arr)
{
    int n = arr.size();
    cout << endl;
    for (int i = 0; i < n; i++)
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

    printArr(arr);

    // bubbleSort(arr);
    // insertionSort(arr);
    // selectionSort(arr);
    // mergePart(arr,0,n-1);
    countPart(arr,0,n-1);


    cout << "\nSorted Array";
    printArr(arr);

    return 0;
}