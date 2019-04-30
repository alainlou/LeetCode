#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> counts;
        for(int num : nums) {
            counts[num] += 1;
        }
        int max = INT_MIN;
        int value = 0;
        for(auto key_value : counts) {
            if(key_value.second > max) {
                max = key_value.second;
                value = key_value.first;
            }
        }
        return value;
    }
};