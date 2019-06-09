#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3) {
            return {};
        }
        set<vector<int>> solution;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 2; ++i) {
            int sum = -nums[i];
            // two pointers solution for two sum
            int left = i + 1;
            int right = nums.size() - 1;
            if(solution.find({-sum, nums[left], nums[right]}) != solution.end()) {
                continue;
            }
            while(left < right) {
                if(nums[left] + nums[right] == sum) {
                    if(solution.find({-sum, nums[left], nums[right]}) == solution.end()) {
                        solution.insert({-sum, nums[left], nums[right]});
                    }
                }
                if(nums[left] + nums[right] < sum) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        vector<vector<int>> result;
        for(vector<int> vec : solution) {
            result.push_back(vec);
        }
        return result;
    }
};