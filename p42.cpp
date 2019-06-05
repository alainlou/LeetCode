#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int counter = 0;
        vector<int> left_max = {0};
        vector<int> right_max = {0};
        int left_carry = 0;
        int right_carry = 0;
        for(int l = 1; l < height.size(); ++l) {
            if(height[l-1] > left_carry) {
                left_carry = height[l-1];
            }
            left_max.push_back(left_carry);
        }
        for(int r = height.size() - 2; r >= 0; --r) {
            if(height[r+1] > right_carry) {
                right_carry = height[r+1];
            }
            right_max.insert(right_max.begin(), right_carry);
        }
        for(int i = 0; i < height.size(); ++i) {
            counter += max(0, min(left_max[i] - height[i], right_max[i] - height[i]));
        }
        return counter;
    }
};