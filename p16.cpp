#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int distance = INT_MAX;
        int sum;
        for(int i = 0; i < nums.size() - 2; ++i) {
            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right) {
                if(abs(target - (nums[i] + nums[left] + nums[right])) < distance) {
                    distance = abs(target - (nums[i] + nums[left] + nums[right]));
                    sum = nums[i] + nums[left] + nums[right];
                }
                if(nums[i] + nums[left] + nums[right] == target) {
                    return target;
                } else if(nums[i] + nums[left] + nums[right] < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return sum;
    }
};