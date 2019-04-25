#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        vector<int> rotated;
        for(int i = nums.size() - k; i < nums.size(); ++i) {
            rotated.push_back(nums[i]);
        }
        for(int j = 0; j < nums.size() - k; ++j) {
            rotated.push_back(nums[j]);
        }
        nums = rotated;
    }
};