#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> answer;
    vector<int> candidates;
    void process(vector<int>& group, int target, int start) {
        if(target == 0) {
            if(find(answer.begin(), answer.end(), group) == answer.end())
                answer.push_back(group);
            return;
        }
        for(int i = start; i < candidates.size() && candidates[i] <= target; ++i) {
            group.push_back(candidates[i]);
            process(group, target - candidates[i], i+1);
            group.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        this->candidates = candidates;
        vector<int> group;
        process(group, target, 0);
        return answer;
    }
};