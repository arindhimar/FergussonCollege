#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib> // For rand() and srand()

using namespace std;

// Merge Sort Functions
void merge(vector<int> &arr, int low, int mid, int high) {
    vector<int> temp;
    int left = low;
    int right = mid + 1;

    while (left <= mid && right <= high) {
        if (arr[left] < arr[right]) {
            temp.push_back(arr[left]);
            left++;
        } else {
            temp.push_back(arr[right]);
            right++;
        }
    }

    while (left <= mid) {
        temp.push_back(arr[left]);
        left++;
    }
    while (right <= high) {
        temp.push_back(arr[right]);
        right++;
    }

    for (int i = 0; i < temp.size(); i++) {
        arr[low + i] = temp[i];
    }
}

void mergeSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

// Quicksort Functions
int quickSort(vector<int> &arr, int low, int high) {
    int pivot = arr[low];
    int i = low + 1;
    int j = high;

    while (i <= j) {
        while (i <= high && arr[i] <= pivot) {
            i++;
        }
        while (j >= low && arr[j] > pivot) {
            j--;
        }
        if (i < j) {
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[j], arr[low]);
    return j;
}

void quickPart(vector<int> &arr, int low, int high) {
    if (low < high) {
        int mid = quickSort(arr, low, high);
        quickPart(arr, low, mid - 1);
        quickPart(arr, mid + 1, high);
    }
}

// Function to print the array
void printArr(const vector<int> &arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    int n, rangeMin, rangeMax;
    cout << "Enter number of elements: ";
    cin >> n;
    cout << "Enter the range for random numbers (min max): ";
    cin >> rangeMin >> rangeMax;

    vector<int> arr(n);
    // Seed the random number generator
    srand(static_cast<unsigned int>(time(0)));

    // Generate random numbers in the specified range
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % (rangeMax - rangeMin + 1) + rangeMin; // Random number between rangeMin and rangeMax
    }

    cout << "Generated Array: ";
    printArr(arr);

    // Sorting using Quicksort
    vector<int> arrQuick = arr; // Copy for Quicksort
    clock_t startQuick = clock();
    quickPart(arrQuick, 0, n - 1);
    clock_t endQuick = clock();
    cout << "Sorted Array using Quicksort: ";
    printArr(arrQuick);
    double durationQuick = double(endQuick - startQuick) / CLOCKS_PER_SEC;
    cout << "Time taken by Quicksort: " << durationQuick << " seconds" << endl;

    
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % (rangeMax - rangeMin + 1) + rangeMin; 
    }

    cout << "Generated Array for Merge Sort: ";
    printArr(arr);

    vector<int> arrMerge = arr; 
    clock_t startMerge = clock();
    mergeSort(arrMerge, 0, n - 1);
    clock_t endMerge = clock();
    cout << "Sorted Array using Merge Sort: ";
    printArr(arrMerge);
    double durationMerge = double(endMerge - startMerge) / CLOCKS_PER_SEC;
    cout << "Time taken by Merge Sort: " << durationMerge << " seconds" << endl;

    return 0;
}