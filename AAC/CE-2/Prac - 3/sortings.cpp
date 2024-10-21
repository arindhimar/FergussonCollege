#include <bits/stdc++.h>
using namespace std;

void bubbleSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
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

        if (min_idx != i)
        {
            swap(arr[i], arr[min_idx]);
        }
    }
}

void mergeSort(vector<int> &arr, int low, int mid, int high)
{
    int l = low;
    int r = mid+1;

    vector<int> temp;

    while (l <= mid && r <= high)
    {
        // cout<<"Yes";

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
        arr[low + i] = temp[i];
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


int quickSort(vector<int> &arr,int low,int high){
    int l = low+1;
    int r = high;
    int p = arr[low];
    while(l<=r){
        while(l<=high && arr[l]<=p){
            l++;
        }
        while(r>=low && arr[r]>p){
            r--;
        }

        if(l<r)swap(arr[l],arr[r]);
    }

    swap(arr[r],arr[low]);

    return r;

}

void quickPart(vector<int> &arr,int low,int high){
    if(low<high){
        int p = quickSort(arr,low,high);
        quickPart(arr,low,p-1);
        quickPart(arr,p+1,high);
    }
}

void countSort(vector<int> &arr){
    int n = arr.size();

    int max = arr[0];

    for(int i=0;i<n;i++){
        if(arr[i]>max){
            max = arr[i];
        }
    }

    vector<int> countArr(max,0);

    for(int i=0;i<n;i++){
        countArr[arr[i]]++;
    }

    for(int i=1;i<n;i++){
        countArr[i]+=countArr[i-1];
    }

    vector<int> OA(n,0);
    for(int i=n-1;i>=0;i--){
        OA[countArr[i-1]]=arr[i];;
        countArr[i]--;
    }

    for(int i=0;i<n;i++){
        arr[i] = OA[i];
    }
}

void printArray(vector<int> &arr)
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

    cout << "OG Array : ";

    printArray(arr);

    // bubbleSort(arr);
    // selectionSort(arr);
    // insertionSort(arr);
    // mergePart(arr, 0, n-1);
    // quickPart(arr,0,n-1);
    // countSort(arr);

    cout << "\nSorted Array : ";

    printArray(arr);

    // cout << "Here";
    return 0;
}