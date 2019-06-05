#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int counter = 0;
        for(int i = 0; i < height.size(); ++i) {
            int left_max = 0;
            int right_max = 0;
            for(int l = i - 1; l >= 0; --l) {
                if(height[l] > left_max) {
                    left_max = height[l];
                }
            }
            for(int r = i + 1; r < height.size(); ++r) {
                if(height[r] > right_max) {
                    right_max = height[r];
                }
            }
            counter += max(0, min(left_max - height[i], right_max - height[i]));
        }
        return counter;
    }
};