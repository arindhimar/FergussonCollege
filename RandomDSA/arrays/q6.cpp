#include <bits/stdc++.h>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int maxArea = 0;

    while (left < right) {
        int currentHeight = min(height[left], height[right]);
        int width = right - left;
        maxArea = max(maxArea, currentHeight * width);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
}

int main() {
    vector<int> height;
    int n;

    cin >> n;
    height.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }

    cout << maxArea(height) << endl;
    return 0;
}
