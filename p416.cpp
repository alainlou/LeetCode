#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        if(nums.size() == 0)
            return false;
        int total_sum = 0;
        for(int n : nums) {
            total_sum += n;
        }
        if(total_sum % 2 != 0)
            return false;
        int target = total_sum/2;

        bool possible[total_sum+1];
        memset(possible, false, sizeof(possible));

        // dp-ish
        for(int n : nums) {
            for(int i = target; i >= n; --i) {
                if(possible[i-n]) {
                    possible[i] = true;
                }
            }
            possible[n] = true;
        }

        return possible[target];
    }
};
