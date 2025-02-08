#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;

    vector<vector<int>> temp1(n, vector<int>(n,0));
    vector<vector<int>> temp2(n, vector<int>(n,0));


    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>temp1[i][j];
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>temp2[i][j];
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            
            cout<<(temp1[i][j]+temp2[i][j])<<" ";
        }
        cout<<endl;
    }

    

    return 0;
}