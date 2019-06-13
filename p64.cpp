#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int dp[n][m];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = grid[0][0];
        for(int i = 1; i < n; ++i) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for(int j = 1; j < m; ++j) {
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        for(int k = 1; k < n; ++k) {
            for(int l = 1; l < m; ++l) {
                dp[k][l] = min(dp[k][l-1], dp[k-1][l]) + grid[k][l];
            }
        }
        return dp[n-1][m-1];
    }
};