#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        for(int i = 1; i < n; ++i) {
            i = max(1, i);
            if(nums[i-1] > nums[i]) {
                swap(nums[i-1], nums[i]);
                i -= 2;
            }
        }
    }
};
