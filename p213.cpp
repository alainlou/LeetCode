#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {        
        if(nums.size() == 0)
            return 0;
        else if(nums.size() == 1)
            return nums[0];
        else if(nums.size() == 2)
            return max(nums[0], nums[1]);
        
        int n = nums.size();
        int dp_start[n-1];
        int dp_end[n];
        
        dp_start[0] = nums[0];
        dp_start[1] = max(dp_start[0], nums[1]);
        for(int i = 2; i < n-1; ++i) {
            dp_start[i] = max(dp_start[i-1], dp_start[i-2] + nums[i]);
        }
        
        dp_end[0] = 0;
        dp_end[1] = nums[1];
        dp_end[2] = max(dp_end[1], nums[2]);
        for(int j = 3; j < n; ++j) {
            dp_end[j] = max(dp_end[j-1], dp_end[j-2] + nums[j]);
        }
        
        return max(dp_start[n-2], dp_end[n-1]);
    }
};