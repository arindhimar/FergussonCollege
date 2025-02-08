#include<bits/stdc++.h>
using namespace std;

void fact(int n) {
    unsigned long long fact = 1; 
    for(int i = 2; i <= n; i++) {
        fact *= i;
    }
    
    cout << "Factorial: " << fact << endl;
}

int main() {
    int n;
    cin >> n;
    fact(n);
    return 0;
}
