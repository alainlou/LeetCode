#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3) {
            return {};
        }
        vector<int> last_added = {-1, -1, -1};
        vector<vector<int>> solution;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 2; ++i) {
            while(i > 0 && i < nums.size() - 3 && (nums[i] == nums[i-1])) {
                ++i;
            }
            if(i > nums.size() - 3) {
                break;
            }
            int sum = -nums[i];
            // two pointers solution for two sum
            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right) {
                if(nums[left] + nums[right] == sum) {
                    if(!(last_added[0] == -sum && last_added[1] == nums[left] && last_added[2] == nums[right])) {
                        solution.push_back({-sum, nums[left], nums[right]});
                        last_added[0] = -sum;
                        last_added[1] = nums[left];
                        last_added[2] = nums[right];
                    }
                }
                if(nums[left] + nums[right] < sum) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return solution;
    }
};