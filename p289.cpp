#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int neighbors(vector<vector<int>>& board, int i, int j) {
        int count = 0;
        // count top
        if(i-1 >= 0) {
            if(j-1 >= 0) count += board[i-1][j-1];
            count += board[i-1][j];
            if(j+1 < board[0].size()) count += board[i-1][j+1];
        }
        // count left
        if(j-1 >= 0) count += board[i][j-1];
        // count right
        if(j+1 < board[0].size()) count += board[i][j+1];
        //count bottom
        if(i+1 < board.size()) {
            if(j-1 >= 0) count += board[i+1][j-1];
            count += board[i+1][j];
            if(j+1 < board[0].size()) count += board[i+1][j+1];
        }
        return count;
    }
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        if(m == 0) {
            return;
        }
        int n = board[0].size();
        vector<vector<int>> copy = board;
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                int n = neighbors(board, i, j);
                if(board[i][j] == 1) {
                    if(n < 2 || n > 3) copy[i][j] = 0;
                } else {
                    if(n == 3) copy[i][j] = 1;
                }
            }
        }
        board = copy;
    }
};