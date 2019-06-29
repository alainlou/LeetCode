#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> solution;
    bool valid(vector<string> &board, int row, int col) {
        // check queen not in same column
        for(int i = 0; i < row; ++i) {
            if(board[i][col] == 'Q')
                return false;
        }
        // check queen not on diagonal (looking upward)
        for(int j = 1; j <= row; ++j) {
            if(board[row-j][col-j] == 'Q' || board[row-j][col+j] == 'Q')
                return false;
        }
        return true;
    }
    void solve(vector<string> &board, int row, int n) {
        // we've reached the end and we're good
        if(row == n) {
            solution.push_back(board);
            return;
        }
        // try placing on any column
        for(int i = 0; i < n; ++i) {
            board[row][i] = 'Q';
            if(valid(board, row, i)) {
                solve(board, row+1, n);
            }
            board[row][i] = '.';
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        string row = "";
        for(int i = 0; i < n; ++i) {
            row += ".";
        }
        vector<string> board;
        for(int j = 0; j < n; ++j) {
            board.push_back(row);
        }
        solve(board, 0, n);
        return solution;
    }
};