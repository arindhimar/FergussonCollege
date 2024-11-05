#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib> // For rand() and srand()
using namespace std;

void bubbleSort(vector<int> &arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void insertionSort(vector<int> &arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void maxHeap(vector<int> &arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        maxHeap(arr, n, largest);
    }
}

void heapSort(vector<int> &arr, int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        maxHeap(arr, n, i);
    }

    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        maxHeap(arr, i, 0);
    }
}

void printArr(const vector<int> &arr) {
    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr(n);
    srand(static_cast<unsigned int>(time(0)));

    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100 + 1;
    }

    cout << "Generated array: ";
    printArr(arr);

    vector<int> arrCopy;

    arrCopy = arr;
    clock_t start = clock();
    bubbleSort(arrCopy);
    clock_t end = clock();
    double bubbleSortTime = double(end - start) / CLOCKS_PER_SEC;
    cout << "Bubble Sort Time: " << bubbleSortTime << " seconds" << endl;

    arrCopy = arr;
    start = clock();
    insertionSort(arrCopy);
    end = clock();
    double insertionSortTime = double(end - start) / CLOCKS_PER_SEC;
    cout << "Insertion Sort Time: " << insertionSortTime << " seconds" << endl;

    arrCopy = arr;
    start = clock();
    heapSort(arrCopy, n);
    end = clock();
    double heapSortTime = double(end - start) / CLOCKS_PER_SEC;
    cout << "Heap Sort Time: " << heapSortTime << " seconds" << endl;

    return 0;
}