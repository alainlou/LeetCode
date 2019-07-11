#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> answer;
    void permute(int& n, vector<int>& curr, vector<int>& nums) {
        if(curr.size() == n) {
            answer.push_back(curr);
            return;
        }
        for(int i = 0; i < nums.size(); ++i) {
            int tmp = nums[i];
            curr.push_back(tmp);
            nums.erase(nums.begin() + i);
            permute(n, curr, nums);
            curr.pop_back();
            nums.insert(nums.begin() + i, tmp);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<int> curr;
        permute(n, curr, nums);
        return answer;
    }
};