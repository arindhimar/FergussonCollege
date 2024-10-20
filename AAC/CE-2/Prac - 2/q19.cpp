#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;

    vector<vector<int>> temp1(n, vector<int>(n, 0));
    vector<vector<int>> temp2(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> temp1[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> temp2[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int temp = 0;
            for (int k = 0; k < n; k++)
            {
                temp+=temp1[i][k]*temp2[k][j];   
            }
            
            cout <<temp << " ";
        }
        cout << endl;
    }

    return 0;
}