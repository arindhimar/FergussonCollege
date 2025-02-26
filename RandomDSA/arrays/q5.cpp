#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v;
    int n;

    cout << "Enter the number of elements: ";
    cin >> n;

    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }


    int target;

    cout << "Enter the target sum: ";
    cin >> target;
    
    sort(v.begin(), v.end());

    int i = 0, j = n - 1;

    while(i < j)
    {
        if(v[i] + v[j] == target)
        {
            cout << v[i] << " " << v[j] << endl;
            i++;
            j--;
        }
        else if(v[i] + v[j] < target)
        {
            i++;
        }
        else
        {
            j--;
        }
    }

    //sample input
    // 5
    // 1 2 3 4 5
    // 5

    return 0;
}