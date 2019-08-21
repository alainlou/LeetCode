#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() == 0)
            return 0;
        int n = height.size();
        int counter = 0;
        int left_max[n];
        int right_max[n];
        left_max[0] = 0;
        right_max[n-1] = 0;
        int left_carry = 0;
        int right_carry = 0;
        for(int l = 1; l < n; ++l) {
            if(height[l-1] > left_carry) {
                left_carry = height[l-1];
            }
            left_max[l] = left_carry;
        }
        for(int r = height.size() - 2; r >= 0; --r) {
            if(height[r+1] > right_carry) {
                right_carry = height[r+1];
            }
            right_max[r] = right_carry;
        }
        for(int i = 0; i < height.size(); ++i) {
            counter += max(0, min(left_max[i] - height[i], right_max[i] - height[i]));
        }
        return counter;
    }
};
