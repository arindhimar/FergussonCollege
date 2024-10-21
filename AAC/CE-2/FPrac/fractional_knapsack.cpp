#include <bits/stdc++.h>
using namespace std;

void frac_knap()
{
    int n;
    cin >> n;

    vector<float> p(n, 0);
    vector<float> w(n, 0);
    vector<float> pbyw(n, 0);
    vector<float> indices(n, 0);

    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
        cin >> w[i];
        if (w[i] != 0)
        {
            pbyw[i] = p[i] / w[i];
        }
        indices[i] = i;
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (pbyw[j + 1] > pbyw[j])
            {
                swap(pbyw[j + 1], pbyw[j]);
                swap(indices[j + 1], indices[j]);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout<<pbyw[i];
    }

    // cout<<"=========";

    float m = 0;
    cin >> m;
    float pr = 0;
    float rem = m;

    for (int i = 0; i < n; i++)
    {
        if (w[indices[i]] <= rem)
        {
            pr += p[indices[i]];
            rem -= w[indices[i]];
        }
        else
        {
            float temp = (rem / w[indices[i]]) * p[indices[i]];
            pr =pr+ temp;
            rem = 0;
        }
    }
    cout << "Profit : " << pr;
}

int main()
{
    frac_knap();
    return 0;
}