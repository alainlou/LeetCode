#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool check(vector<int>& nums) {
        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] < nums[i-1])
                return false;
        }
        return true;
    }
    bool checkPossibility(vector<int>& nums) {
        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] < nums[i-1]) {
                bool answer = false;
                // try editing nums[i-1]
                int lim = ((i-2)>=0) ? nums[i-2] : nums[i]-1;
                for(int j = nums[i]; j >= lim; --j) {
                    int old = nums[i-1];
                    nums[i-1] = j;
                    if(check(nums)) {
                        answer = true;
                        break;
                    }
                    nums[i-1] = old;
                }
                // try editing nums[i]
                lim = ((i+1)<nums.size()) ? nums[i+1] : nums[i-1]+1;
                for(int j = nums[i-1]; j <= lim; ++j) {
                    int old = nums[i];
                    nums[i] = j;
                    if(check(nums)) {
                        answer = true;
                        break;
                    }
                    nums[i] = old;
                }
                if(answer == false)
                    return false;
            }
        }
        return true;
    }
};
