#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> solution;
    void generate(vector<int> curr, vector<int>& candidates, int target, int i, int& n) {
        if(target < 0)
            return;
        if(curr.size() >= n) {
            if(target == 0)
                solution.push_back(curr);
            return;
        }
        vector<int> alt1 = curr;
        alt1.push_back(candidates[i]);
        generate(alt1, candidates, target-candidates[i], i, n);
        if(i < candidates.size() - 1) {
            vector<int> alt2 = curr;
            generate(alt2, candidates, target, i+1, n);
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        // this is the upper limit for size of one group
        int n = target/candidates[0];
        // generate all possible permutations and verify
        for(int size = 1; size <= n; ++size) {
            for(int start = 0; start < candidates.size(); ++start) {  
                generate({candidates[start]}, candidates, target-candidates[start], start, size);
            }
        }
        return solution;
    }
};