#include<bits/stdc++.h>
using namespace std;
int main()
{
    string str = "Hello World";
    string xor_str = "";
    for (char c : str) {
        // cout << (c ^ 0);
        xor_str += c ^ 0;
    }
    cout << xor_str << endl;
    xor_str="";
    for (char c : str) {
        // cout << (c ^ 0);
        xor_str += c ^ 1;
    }

    cout << xor_str << endl;
    return 0;
}