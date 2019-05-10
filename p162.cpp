#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if(nums.size() == 1) {
            return 0;
        } else if (nums.size() == 2) {
            return nums[0] > nums[1] ? 0 : 1;
        } else if (nums[nums.size() - 1] > nums[nums.size() - 2]) {
            return nums.size() - 1;
        } else if (nums[0] > nums[1]) {
            return 0;
        }
        int low = 0;
        int high = nums.size() - 1;
        int curr = (high - low) / 2;
        while(true) {
            if(nums[curr] > nums[curr + 1] && nums[curr] > nums[curr-1]) {
                return curr;
            } else if (nums[curr + 1] > nums[curr]) {
                low = curr;
                curr = (high - low) / 2 + low;
            } else {
                high = curr;
                curr = (high - low) / 2 + low;
            }
        }
    }
};