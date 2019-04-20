#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int num_zero = count(nums.begin(), nums.end(), 0);
        for(int i {0}; i < nums.size() - num_zero; ++i){
            if(nums[i] == 0){
                nums.push_back(0);
                nums.erase(nums.begin() + i);
                --i;
            }
        }
    }
};