#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        else if(nums.size() == 1)
            return nums[0];
        vector<int> result;
        result.push_back(nums[0]);
        result.push_back(max(nums[0], nums[1]));
        for(int i = 2; i < nums.size(); ++i) {
            result.push_back(max(nums[i] + result[i-2], result[i-1]));
        }
        
        return result[result.size() - 1];
    }
};