#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        if(nums.size() == 0)
            return {};
        sort(nums.begin(), nums.end());
        vector<int> result;
        for(int i = 1; i < nums[0]; ++i) {
            result.push_back(i);
        }
        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] > nums[i-1] + 1) {
                for(int j = nums[i-1]+1; j < nums[i]; ++j) {
                    result.push_back(j);
                }
            }
        }
        for(int i = nums[nums.size()-1]+1; i <= nums.size(); ++i) {
            result.push_back(i);
        }
        return result;
    }
};