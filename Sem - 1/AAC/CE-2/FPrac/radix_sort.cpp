#include <bits/stdc++.h>
using namespace std;

int getMax(vector<int> &arr, int n) {
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}

void countSort(vector<int> &arr, int n, int exp) {
    int countArr[10] = {0}; // Fixed size for counting digits (0-9)
    vector<int> oa(n);      // Output array to store the sorted numbers

    // Store count of occurrences for each digit
    for (int i = 0; i < n; i++) {
        countArr[(arr[i] / exp) % 10]++;
    }

    // Change countArr so that it now contains the actual position of digits
    for (int i = 1; i < 10; i++) {
        countArr[i] += countArr[i - 1];
    }

    // Build the output array by placing elements in the correct position
    for (int i = n - 1; i >= 0; i--) {
        oa[countArr[(arr[i] / exp) % 10] - 1] = arr[i];
        countArr[(arr[i] / exp) % 10]--;
    }

    // Copy the sorted numbers back to the original array
    for (int i = 0; i < n; i++) {
        arr[i] = oa[i];
    }

    // Optionally print the array after this digit has been sorted
    cout << "Array after sorting on digit place " << exp << ": ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void radix_sort() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int m = getMax(arr, n); // Find the maximum number to determine the number of digits

    // Do counting sort for each digit position (exp = 1, 10, 100, etc.)
    for (int exp = 1; m / exp > 0; exp *= 10) {
        countSort(arr, n, exp);
    }

    // Print the final sorted array
    cout << "Final sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    radix_sort();
    return 0;
}
