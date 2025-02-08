#include <bits/stdc++.h>
using namespace std;

void sort(vector<int> &arr)
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

void binSe(vector<int> &arr)
{
    int n = arr.size();
    int k;

    cin >> k;

    int low = 0;
    int high = n;
    while (low <= high)
    {
        int mid =(high + low) / 2;

        if (arr[mid] == k)
        {
            cout << mid;
            return;
        }

        if (arr[mid] < k)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    cout << "None";
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
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    sort(arr);

    printArray(arr);

    binSe(arr);

    return 0;
}