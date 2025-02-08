#include <bits/stdc++.h>
using namespace std;

void matrix_multiply()
{
    int n;
    cin >> n;

    int m1[n][n];
    int m2[n][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {

            cin >> m1[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {

            cin >> m2[i][j];
        }
    }

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++){
            cout<<m1[i][j]+m2[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main()
{
    matrix_multiply();
    return 0;
}