#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // first, find out which digit to increment
        // then, flip all of the digits to the right of that digit (minimize)
        int n = nums.size();
        int to_incr = -1;
        for(int i = n-1; i > 0; --i) {
            // this is the first digit that doesn't form a max permutation
            if(nums[i-1] < nums[i]) {
                to_incr = i-1;
                break;
            }
        }
        // find where to swap it
        if(to_incr != -1) {
            for(int j = to_incr+1; j < n; ++j) {
                if(nums[j] > nums[to_incr] && (j == n-1 || nums[j+1] <= nums[to_incr])) {
                    swap(nums[to_incr], nums[j]);
                    break;
                }
            }
        }
        
        // flip all the rest of it
        for(int i = 0; i < (n-to_incr)/2; ++i) {
            swap(nums[i+1+to_incr], nums[n-1-i]);
        }
    }
};
