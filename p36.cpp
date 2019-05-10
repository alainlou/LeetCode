#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(vector<char> row: board) {
            set<char> contained;
            for(char c : row) {
                if(contained.find(c) != contained.end()) {
                    return false;
                } else if (c != '.') {
                    contained.insert(c);
                }
            }
        }
        for(int col = 0; col < 9; ++col) {
            set<char> contained;
            for(int row = 0; row < 9; ++row) {
                if(contained.find(board[row][col]) != contained.end()) {
                    return false;
                } else if (board[row][col] != '.') {
                    contained.insert(board[row][col]);
                }
            }
        }
        int starting_points[9][2] = {
            {0, 0}, {0, 3}, {0, 6},
            {3, 0}, {3, 3}, {3, 6},
            {6, 0}, {6, 3}, {6, 6}
        };
        for(int box = 0; box < 9; ++box) {
            set<char> contained;
            for(int row = 0; row < 3; ++row) {
                for(int col = 0; col < 3; ++col) {
                    int r = row + starting_points[box][0];
                    int c = col + starting_points[box][1];
                    if(contained.find(board[r][c]) != contained.end()) {
                        return false;
                    } else if(board[r][c] != '.') {
                        contained.insert(board[r][c]);
                    }
                }
            }
            
        }
        return true;
    }
};