#include <bits/stdc++.h>
using namespace std;

void magicSquare(int n)
{
    int r = 0;
    int c = n / 2;

    vector<vector<int>> temp(n, vector<int>(n, 0));

    for (int i = 1; i <= n * n; i++)
    {
        temp[r][c] = i;

        int nr = ((n + r) - 1) % n;
        int nc = ((n + c) - 1) % n;

        if (temp[nr][nc] != 0)
        {
            r = (r + 1) % n;
        }
        else
        {
            r = nr;
            c = nc;
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<temp[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main()
{
    int n;
    cin>>n;
    if (n % 2 != 0)
    {
        magicSquare(n);
    }
    return 0;
}