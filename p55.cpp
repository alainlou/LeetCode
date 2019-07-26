#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i = 0;
        int end_index = nums[0];
        while(i <= end_index && i < nums.size()) {
            end_index = max(end_index, nums[i]+i);
            ++i;
        }
        return end_index >= nums.size()-1;
    }
};