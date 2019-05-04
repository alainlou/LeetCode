#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = INT_MIN;
        int curr_sum = INT_MIN;
        for(int n : nums) {
            if(curr_sum > 0) {
                curr_sum += n;
                if(curr_sum < 0) {
                    curr_sum = 0;
                }
            } 
            if(n > curr_sum) {
                curr_sum = n;
            }
            if(curr_sum > max) {
                max = curr_sum;
            }
        }
        return max;
    }
};