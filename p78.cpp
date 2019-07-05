#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> solution = {};
        int n = nums.size();
        for(unsigned int i = 0; i < pow(2, n); ++i) {
            vector<int> subset;
            // digits of the binary number i describe whether the element is in this current subset or not
            for(int j = 0; j < n; ++j) {
                int mask = 1 << j;
                // the digit is a '1'
                if((i&mask) > 0)
                    subset.push_back(nums[j]);
            }
            solution.push_back(subset);
        }
        return solution;
    }
};