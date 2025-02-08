#include <bits/stdc++.h>
using namespace std;

// Function to calculate factorial of a number
int factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; ++i) {
        fact *= i; // Multiply current number with fact
    }
    return fact; // Return the calculated factorial
}

// Function to calculate nCr (combination)
int nCr(int n, int r) {
    // nCr = n! / (r! * (n-r)!)
    return factorial(n) / (factorial(r) * factorial(n - r));
}

// Function to print the expansion of the Binomial Theorem (a + b)^n
void printBinomialTheorem(int n) {
    // Check for invalid input
    if (n < 0) {
        cout << "Invalid input" << endl;
        return;
    }

    // Loop through each term in the expansion
    for (int i = 0; i <= n; ++i) {
        // Calculate the coefficient for the current term
        int coeff = nCr(n, i);
        cout << coeff; // Print the coefficient

        // Append the power of 'a' if it exists
        if (n - i > 0) 
            cout << "a^" << (n - i);

        // Append the power of 'b' if it exists
        if (i > 0) 
            cout << "b^" << i;

        // Print a "+" unless it's the last term
        if (i < n) 
            cout << " + ";
    }
    cout << endl; // End the expansion with a newline
}

int main() {
    int n;
    // Input the power 'n' for the expansion
    cin >> n;

    // Print the expansion of (a + b)^n
    printBinomialTheorem(n);

    return 0; // Return success
}
