#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int after[n];
        after[n-1] = nums[n-1];
        for(int j = nums.size()-2; j >= 0; --j) {
            after[j] = nums[j]*after[j+1];
        }
        vector<int> output;
        int accumulate = nums[0];
        output.push_back(after[1]);
        for(int k = 1; k < nums.size()-1; ++k) {
            output.push_back(accumulate * after[k+1]);
            accumulate *= nums[k];
        }
        output.push_back(accumulate);
        return output;
    }
};