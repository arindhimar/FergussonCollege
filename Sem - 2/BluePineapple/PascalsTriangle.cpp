#include <bits/stdc++.h>
using namespace std;

// Function to calculate factorial
int factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; ++i) {
        fact *= i;
    }
    return fact;
}

// Function to calculate nCr
int nCr(int n, int r) {
    return factorial(n) / (factorial(r) * factorial(n - r));
}

// Function to print Pascal's Triangle with proper alignment
void printPascalsTriangle(int n) {
    if (n <= 0) {
        cout << "Invalid input" << endl;
        return;
    }
    for (int i = 0; i < n; ++i) {
        // Print leading spaces for alignment
        for (int spaces = 0; spaces < n - i - 1; ++spaces) {
            cout << " ";
        }
        // Print numbers in the current row
        for (int j = 0; j <= i; ++j) {
            cout << nCr(i, j) << " ";
        }
        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;
    printPascalsTriangle(n);
    return 0;
}