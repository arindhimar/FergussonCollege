#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums;
    
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        nums.push_back(temp);
    }

    int lastNonZeroFoundAt = 0;

    for (int i = 0; i < n; i++) {
        if (nums[i] != 0) {
            nums[lastNonZeroFoundAt] = nums[i];
            lastNonZeroFoundAt++;
        }
    }

    for (int i = lastNonZeroFoundAt; i < n; i++) {
        nums[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        cout << nums[i] << " ";
    }

    return 0;
}