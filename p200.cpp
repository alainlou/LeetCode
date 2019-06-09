#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void fill(vector<vector<char>>& grid, int row, int col) {
        bool out_of_bounds = row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size();
        if(out_of_bounds || grid[row][col] == '0') {
            return;
        }
        grid[row][col] = '0';
        fill(grid, row+1, col);
        fill(grid, row-1, col);
        fill(grid, row, col+1);
        fill(grid, row, col-1);
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid[0].size(); ++j) {
                if(grid[i][j] == '1') {
                    ++count;
                    fill(grid, i, j);
                }
            }
        }
        return count;
    }
};