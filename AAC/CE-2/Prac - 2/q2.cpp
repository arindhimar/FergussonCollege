#include <bits/stdc++.h>
using namespace std;

void fibo(int n)
{
    if (n == 1)
    {
        cout << "0" << endl;
        return;
    }
    if (n == 2)
    {
        cout << " 0 1" << endl;
        return;
    }

    int a = 0;
    int b = 1;
    cout << a << " " << b;
    for (int i = 2; i <= n; i++)
    {
        int c = a + b;
        cout << " " << c;
        a = b;
        b = c;
    }
}

int recur_fibo(int n)
{
    if (n <= 0)
        return 0;
    if (n == 1)
        return 0;
    if (n == 2)
        return 1;

    return recur_fibo(n - 1) + recur_fibo(n - 2);
}

int main()
{
    fibo(5);
    cout<<endl;
    cout<<recur_fibo(5+1);
    return 0;
}