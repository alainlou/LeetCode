#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int count = 0;
        for(int i = n-1; i >= 2; --i) {
            for(int j = i-1; j >= 1; --j) {
                if(nums[i] >= nums[j] + nums[j-1]) {
                    continue;
                }
                for(int k = j-1; k >= 0; --k) {
                    if(nums[i] < nums[j] + nums[k]) {
                        ++count;
                    } else {
                        break;
                    }
                }
            }
        }
        return count;
    }
};

