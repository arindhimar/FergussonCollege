#include <iostream>
using namespace std;

#define N 8

void printBoard(int board[N][N]) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << (board[i][j] ? "Q " : ". ");
        }
        cout << endl;
    }
    cout << endl;
}

bool isSafe(int board[N][N], int row, int col) {
    cout<<"==New Wala"<<endl;
    for (int i = 0; i < row; ++i) {
        // cout<<"hmmmmmmm==========="<<i<<col<<endl; vertical boxes checking all the prev one's
        if (board[i][col]) return false; // Check column
    }
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j) {
        // cout<<"Loop 2 ->"<<i+1<<j+1<<endl;
        if (board[i][j]) return false; // Check left diagonal
    }
    for (int i = row - 1, j = col + 1; i >= 0 && j < N; --i, ++j) {
        // cout<<"Loop3 ->"<<i+1<<j+1<<endl;
        if (board[i][j]) return false; // Check right diagonal
    }
    return true;
}

bool solveNQueens(int board[N][N], int row) {
    if (row == N) { 
        return true;
    }

    for (int col = 0; col < N; ++col) {
        // cout<<"Solve wale rowss & colsss"<<row<<col;
        if (isSafe(board, row, col)) {
            board[row][col] = 1; 
            printBoard(board);  
            if (solveNQueens(board, row + 1)) { // Recursive call
                return true;
            }
            board[row][col] = 0; // Backtrack
        }
    }

    return false; 
}

int main() {
    int board[N][N] = {0};
    if (!solveNQueens(board, 0)) {
        cout << "No solution found" << endl;
    }
    return 0;
}

