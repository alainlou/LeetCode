#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int n = nums.size();
        int dp[n][3];
        memset(dp[0], 0, sizeof(dp[0]));
        if(nums[0]%3 == 0)
            dp[0][0] = nums[0];
        else if(nums[0]%3 == 1)
            dp[0][1] = nums[0];
        else
            dp[0][2] = nums[0];
        for(int i = 1; i < n; ++i) {
            if(nums[i]%3 == 0) {
                dp[i][0] = dp[i-1][0]+nums[i];
                dp[i][1] = dp[i-1][1] != 0 ? dp[i-1][1]+nums[i] : dp[i-1][1];
                dp[i][2] = dp[i-1][2] != 0 ? dp[i-1][2]+nums[i] : dp[i-1][2];
            } else if(nums[i]%3 == 1) {
                dp[i][0] = dp[i-1][2] != 0 ? max(dp[i-1][2]+nums[i], dp[i-1][0]) : dp[i-1][0];
                dp[i][1] = max(dp[i-1][0]+nums[i], dp[i-1][1]);
                dp[i][2] = dp[i-1][1] != 0 ? max(dp[i-1][1]+nums[i], dp[i-1][2]) : dp[i-1][2];
            } else {
                dp[i][0] = dp[i-1][1] != 0 ? max(dp[i-1][1]+nums[i], dp[i-1][0]) : dp[i-1][0];
                dp[i][1] = dp[i-1][2] != 0 ? max(dp[i-1][2]+nums[i], dp[i-1][1]) : dp[i-1][1];
                dp[i][2] = max(dp[i-1][0]+nums[i], dp[i-1][2]);
            }
        }
        return dp[n-1][0];
    }
};