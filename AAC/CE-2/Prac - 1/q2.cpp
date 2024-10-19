#include <iostream>
using namespace std;

void fibo(int n) {
    int a = 0;
    int b = 1;
    int c;
    if (n >= 1) cout << a;
    if (n >= 2) cout << " " << b;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
        cout << " " << c;
    }
    cout << endl;
}

int nthFibonacci(int n){
    if (n <= 1){
        return n;
    }
    return nthFibonacci(n - 1) + nthFibonacci(n - 2);
}



int main() {
    int n;
    cout << "Enter the number of Fibonacci terms: ";
    cin >> n;

    cout << "Iterative Fibonacci: ";
    fibo(n);

    cout << "Recursive Fibonacci: "<<nthFibonacci(n);
    

    return 0;
}