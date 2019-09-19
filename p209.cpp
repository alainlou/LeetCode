#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        if(n == 0)
            return 0;
        int carry = nums[0];
        int left = 0;
        int right = 0;
        int result = INT_MAX;
        while(right < n) {
            if(carry < s) {
                ++right;
                if(right > n-1) break;
                carry += nums[right];
            } else {
                result = min(result, right-left+1);
                carry -= nums[left];
                ++left;
            }
        }
        return (result == INT_MAX) ? 0 : result;
    }
};
