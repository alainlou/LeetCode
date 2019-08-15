#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    map<pair<int, int>, int> memo;
    int count(vector<int>& nums, int &S, int curr, int i) {
        if(memo.find({curr, i}) != end(memo)) {
            return memo[{curr, i}];
        }
        if(i >= nums.size())
            return curr == S;
        int r1 = count(nums, S, curr+nums[i], i+1);
        int r2 = count(nums, S, curr-nums[i], i+1);
        memo[{curr, i}] = r1+r2;
        return r1+r2;        
    }
    int findTargetSumWays(vector<int>& nums, int S) {
        return count(nums, S, 0, 0);        
    }
};
