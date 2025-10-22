#include <bits/stdc++.h>
using namespace std;

void setZero(vector<vector<int>>& matrix, int row, int col) {
    int r = matrix.size();
    int c = matrix[0].size();

    for (int j = 0; j < c; ++j) {
        matrix[row][j] = 0;
    }

    for (int i = 0; i < r; ++i) {
        matrix[i][col] = 0;
    }
}

int main() {
    vector<vector<int>> matrix = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    int n = matrix.size();
    int m = matrix[0].size();

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (matrix[i][j] == 0) {
                setZero(matrix, i, j);
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
