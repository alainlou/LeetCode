#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> left_sum(n+1, 0);
        left_sum[0] = 0;
        for(int i = 1; i < n+1; ++i) {
            left_sum[i] = nums[i-1] + left_sum[i-1];
        }
        int count = 0;
        for(int i = 0; i < n; ++i) {
            for(int j = i+1; j < n+1; ++j) {
                if(left_sum[j] - left_sum[i] == k)
                    ++count;
            }
        }
        return count;
    }
};
