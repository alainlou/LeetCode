#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int curr = 1;
        int result = nums.size() > 0 ? 1 : 0;
        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] <= nums[i-1]) {
                curr = 1;
            } else {
                ++curr;
            }
            if(curr > result)
                result = curr;
        }
        return result;
    }
};