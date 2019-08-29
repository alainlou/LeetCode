#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int n = matrix.size();
        if(n == 0) return 0;        
        int m = matrix[0].size();
        
        int dp[n][m];
        memset(dp, 0, sizeof(dp));
        
        int answer = 0;
        
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if(matrix[i][j] == '1') {
                    dp[i][j] = 1;
                    // check if we can extend a square
                    if(i > 0 && j > 0 && dp[i-1][j-1] > 0) {
                        int l = dp[i-1][j-1];
                        int s = 0;
                        for(int k = 1; k <= l; ++k) {
                            if(matrix[i-k][j] == '0' || matrix[i][j-k] == '0') {
                                break;
                            } else {
                                ++s;
                            }
                        }
                        dp[i][j] = s+1;
                    }
                }
                answer = max(answer, dp[i][j]*dp[i][j]);
            }
        }
        
        return answer;
    }
};
