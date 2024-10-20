#include <bits/stdc++.h>
using namespace std;

void perfectNumber(int n)
{
    // cout<<"Asdaskjd";

    int sum = 0;
    for (int i = 1; i <n; i++)
    {
    // cout<<"Asdaskjd";

        if (n % i == 0)
        {
            sum += i;
                // cout<<"Sum : "<<sum;

        }
    }
    if (sum == n)
    {
        cout << "Yes";
    }
    else
    {
        cout << "NO";
    }
}

int main()
{
    int n;
    cin >> n;
    perfectNumber(n);
    return 0;
}