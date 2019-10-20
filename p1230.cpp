#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    double probabilityOfHeads(vector<double>& prob, int target) {
        int n = prob.size();
        double dp[target+1][n];
        dp[0][0] = 1-prob[0];
        for(int i = 1; i < n; ++i) {
            dp[0][i] = dp[0][i-1]*(1-prob[i]);
        }
        if(target > 0)
            dp[1][0] = prob[0];
        for(int i = 2; i < target+1; ++i) {
            dp[i][0] = 0;
        }
        for(int i = 1; i < target+1; ++i) {
            for(int j = 1; j < n; ++j) {
                dp[i][j] = dp[i][j-1]*(1-prob[j]) + dp[i-1][j-1]*prob[j];
            }
        }
        return dp[target][n-1];
    }
};

