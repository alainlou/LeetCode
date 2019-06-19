#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        unsigned int dp[m][n];
        memset(dp, 0, sizeof(dp));
        dp[0][0] = obstacleGrid[0][0] ? 0 : 1;
        for(int i = 1; i < m; ++i) {
            if(!obstacleGrid[i][0])
                dp[i][0] = dp[i-1][0];
        }
        for(int j = 1; j < n; ++j) {
            if(!obstacleGrid[0][j])
                dp[0][j] = dp[0][j-1];
        }
        for(int k = 1; k < m; ++k) {
            for(int l = 1; l < n; ++l) {
                if(!obstacleGrid[k][l])
                    dp[k][l] = dp[k-1][l] + dp[k][l-1];
            }
        }
        return dp[m-1][n-1];
    }
};