#include <bits/stdc++.h>
using namespace std;

void fractionalKnapSack(int n)
{
    vector<int> p(n);
    vector<int> w(n);
    vector<float> pbyw(n);
    vector<int> indices(n);

    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
        cin >> w[i];
        if (w[i] != 0)
        {
            pbyw[i] = static_cast<float>(p[i]) / w[i];
        }
        else
        {
            pbyw[i] = 0;
        }
        indices[i] = i;
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (pbyw[j + 1] > pbyw[j])
            {
                swap(pbyw[j + 1], pbyw[j]);
                swap(indices[j + 1], indices[j]);
            }
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     cout << "===" << pbyw[i] << endl;
    // }

    int m;
    cout << "Enter total capacity: ";
    cin >> m;
    float rem = m;
    float profit = 0;
    for (int i = 0; i < n; i++)
    {
        if (w[indices[i]] <= rem)
        {
            profit += p[indices[i]];
            rem -= w[indices[i]];
        }
        else
        {
            // cout<<((rem / w[indices[i]]) * p[indices[i]]) ;
            profit += (rem / w[indices[i]]) * p[indices[i]];

            break;
        }
        // cout << "==profit" << profit << "=-=" << endl;
    }

    cout << "Profit: " << profit << endl;
}

int main()
{
    int n;
    cin >> n;
    fractionalKnapSack(n);
    return 0;
}