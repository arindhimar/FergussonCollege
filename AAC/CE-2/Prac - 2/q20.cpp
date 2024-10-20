#include <iostream>
using namespace std;

long long power(int base, int exp) {
    if (exp == 0) return 1; 
    long long half = power(base, exp / 2);
    if (exp % 2 == 0) {
        return half * half; 
    } else {
        return base * half * half;
    }
}

int main() {
    int base, exp;
    cout << "Enter base and exponent: ";
    cin >> base >> exp;
    cout << base << "^" << exp << " = " << power(base, exp) << endl;
    return 0;
}

//dry run
// 2 5
// =
// exp != 0 
// power(2,5)
// =
// =
// exp != 0 
// power(2,2)
// =
// exp!=0
// power(2,1)
// =
// power(2,0)
// return 1;
// =
// power(2,1)
// return 2*1*1
// =
// power(2,2)
// return 2*2
// =
// power(2,5)
// return 2*4*4 = 32
// =

