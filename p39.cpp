#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> solution;
    vector<int> candidates;
    void generate(vector<int>& curr, int target, int start) {
        if(target == 0) {
            solution.push_back(curr);
        }
        for(int i = start; i < candidates.size() && candidates[i] <= target; ++i) {
            curr.push_back(candidates[i]);
            generate(curr, target - candidates[i], i);
            curr.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        this->candidates = candidates;
        vector<int> tmp;
        generate(tmp, target, 0);
        return solution;
    }
};