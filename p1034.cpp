#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void print_2d(vector<vector<int>> &vec) {
        for(vector<int> row : vec) {
            for(int num : row) {
                cout << num << " ";
            }
            cout << endl;
        }
    }
    void color_in(vector<vector<int>> &copy, vector<vector<bool>> &visited, vector<vector<int>> &grid, int row, int col, int &color, int &old, int &num_rows, int &num_cols) {
        // is it out of bounds
        if(row < 0 || row > num_rows - 1 || col < 0 || col > num_cols - 1) {
            return;
        }
        if(visited[row][col]) {
            return;
        }
        visited[row][col] = true;
        // is it not the same component
        if(grid[row][col] != old) {
            return;
        }
        // is it an edge?
        bool is_edge = row == 0 || row == num_rows - 1 || col == 0 || col == num_cols - 1;
        // is it a border
        bool is_border = is_edge || copy[row][col+1] != old || copy[row][col-1] != old || copy[row+1][col] != old || copy[row-1][col] != old;
        if(is_border) {
            grid[row][col] = color;
        }
        color_in(copy, visited, grid, row, col+1, color, old, num_rows, num_cols);
        color_in(copy, visited, grid, row, col-1, color, old, num_rows, num_cols);
        color_in(copy, visited, grid, row-1, col, color, old, num_rows, num_cols);
        color_in(copy, visited, grid, row+1, col, color, old, num_rows, num_cols);
    }
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0, int color) {
        vector<vector<bool>> visited;
        vector<vector<int>> copy;
        for(vector<int> row : grid) {
            copy.push_back(row);
        }
        // record color of component
        int old = grid[r0][c0];
        if(color == old) {
            return grid;
        }
        int num_rows = grid.size();
        int num_cols = grid[0].size();
        vector<bool> fill;
        for(int i = 0; i < num_cols; ++i) {
            fill.push_back(false);
        }
        for(int j = 0; j < num_rows; ++j) {
            visited.push_back(fill);
        }
        color_in(copy, visited, grid, r0, c0, color, old, num_rows, num_cols);
        return grid;
    }
};