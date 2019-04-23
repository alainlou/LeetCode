#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> exists;
        for(int i {0}; i < nums.size(); ++i) {
            if(exists.count(nums[i]) > 0) {
                return true;
            }
            exists[nums[i]] = true; 
        }
        return false;
    }
};