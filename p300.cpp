#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        int answer = 0;
        vector<int> dp(n, 0);
        dp[0] = 1;
        for(int i = 1; i < n; ++i) {
            int take_it = 0;
            for(int j = i-1; j >= 0; --j) {
                if(nums[j] < nums[i])
                    take_it = max(take_it, dp[j]);
            }
            dp[i] = 1 + take_it;
        }
        for(int i : dp) {
            answer = max(answer, i);
        }
        return answer;
    }
};
