#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;

    cin >> n;

    int arr[n][n] = {0};

    int r = 0;
    int c = n / 2;

    for (int i = 1; i <= n * n; i++)
    {
        arr[r][c]=i;

        int nr = ((n+r)-1)%n;
        int nc = ((n+c)-1)%n;

        if(arr[nr][nc]!=0){
            r=(r+1)%n;
        }
        else{
            r=nr;
            c=nc;
        }
    }

    return 0;
}


