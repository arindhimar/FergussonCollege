#include <bits/stdc++.h>
using namespace std;

int main() {
    string s = "()(()())(())";
    string r = "";
    int l = 0;

    for (char c : s) {
        if (c == '(') {
            l++;
            if (l > 1) r += c; 
        } else {
            if (l > 1) r += c; 
            l--;
        }
    }

    cout << r;
    return 0;
}
