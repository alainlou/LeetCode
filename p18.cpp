#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    set<vector<int>> solutions = {};
    void solve(vector<int>& nums, int start, int end, int target) {
        if(start > end - 2) {
            return;
        }
        // two pointers
        int left = start + 1;
        int right = end - 1;
        while(left < right) {
            int sum = nums[start] + nums[left] + nums[right] + nums[end];
            vector<int> solution = {nums[start], nums[left], nums[right], nums[end]};
            if(sum == target){
                solutions.insert(solution);
                ++left;
            } else if(sum < target) {
                ++left;
            } else {
                --right;
            }
        }
    }
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if(nums.size() < 4)
            return {};
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 3; ++i) {
            for(int j = i + 3; j < nums.size(); ++j) {
                solve(nums, i, j, target);
            }
        }
        vector<vector<int>> result;
        for(vector<int> solution : solutions) {
            result.push_back(solution);
        }
        return result;
    }
};