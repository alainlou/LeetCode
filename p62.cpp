#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        int grid [m][n];
        memset(grid, 0, sizeof(grid));
        
        for(int i {0}; i < m; ++i) {
            grid[i][0] = 1;
        }
        for(int j {0}; j < n; ++j) {
            grid[0][j] = 1;
        }
        for(int k {1}; k < m; ++k) {
            for(int l{1}; l < n; ++l) {
                grid[k][l] = grid[k-1][l] + grid[k][l-1];
            }
        }
        
        return grid[m-1][n-1];
    }
};