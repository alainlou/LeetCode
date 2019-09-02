#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int compute(vector<int>& nums, int left, int right, int k, vector<vector<int>>& dp) {
        int result = 0;
        if(k > left)
            result += dp[left][k-1];
        if(k < right)
            result += dp[k+1][right];        
        int pop = nums[k];
        if(left > 0)
            pop *= nums[left-1];
        if(right < nums.size()-1)
            pop *= nums[right+1];
        result += pop;        
        return result;
    }
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        if(n == 0)
            return 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        // extend the length of subarray by i
        for(int i = 0; i < n; ++i) {
            // extend the subarray starting at j
            for(int j = 0; j < n-i; ++j) {
                // consider all the possibilities for last balloon to burst
                int left = j;
                int right = j+i;
                int best = 0;
                for(int k = left; k <= right; ++k) {
                    best = max(best, compute(nums, left, right, k, dp));
                }
                dp[left][right] = best;
            }
        }
        return dp[0][n-1];
    }
};
