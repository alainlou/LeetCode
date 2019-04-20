#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void mark(vector<vector<char>>& grid, vector<vector<bool>>& visited, int i, int j) {
        if(i >= grid.size() || j >= grid[0].size() || i < 0 || j < 0 ||
           grid[i][j] == '0' ||
           visited[i][j]
          ) {
            return;
        } else {
            visited[i][j] = true;
            mark(grid, visited, i+1, j);
            mark(grid, visited, i-1, j);
            mark(grid, visited, i, j+1);
            mark(grid, visited, i, j-1);            
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0) {
            return 0;
        }
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
        int counter = 0;
        for(int i {0}; i < grid.size(); ++i) {
            for(int j {0}; j < grid[0].size(); ++j) {
                if(grid[i][j] == '1' && !visited[i][j]) {
                    ++counter;
                    mark(grid, visited, i, j);
                }
            }
        }
        return counter;
    }
};