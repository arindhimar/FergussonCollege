#include <bits/stdc++.h>
using namespace std;

void fractionalKnapSack()
{
    int n;
    cin>>n;
    vector<float> p(n);
    vector<float> w(n);
    vector<float> pw(n);
    vector<int> idx(n);

    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
        cin >> w[i];
        if (w[i] != 0)
        {
            pw[i] = p[i] / w[i];
        }
        idx[i] = i;
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (pw[j + 1] > pw[j])
            {
                swap(pw[j + 1], pw[j]);
                swap(idx[j + 1], idx[j]);
            }
        }
    }

    int m;
    cout << "enter capacity       ";
    cin >> m;

    int rem = m;

    int profit = 0;

    for (int i = 0; i < n; i++)
    {
        if(w[idx[i]]<=rem){
            profit+=p[idx[i]];
            rem -=w[idx[i]];
        }
        else{
            int temp = (rem/w[idx[i]])*p[idx[i]];
            profit+=temp;

        }
    }

    cout<<"Profit : "<<profit;
}

int main()
{
    fractionalKnapSack();
    return 0;
}