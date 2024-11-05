#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;

    int m1[n][n],m2[n][n];

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>m1[i][j];
        }
    }


    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>m2[i][j];
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int temp = 0;
            for(int k=0;k<n;k++){
                temp +=m1[i][k]*m2[k][j];
            }
            cout<<temp<<" ";
        }
        cout<<endl;
    }

    return 0;
}