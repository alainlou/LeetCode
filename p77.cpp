#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> solutions;
    void process(vector<int> &solution, int start, int k, int &n) {
        if(k == 0) {
            solutions.push_back(solution);
            return;
        }
        for(int i = start; i <= n-k+1; ++i) {
            solution.push_back(i);
            process(solution, i+1, k-1, n);
            solution.erase(solution.begin()+solution.size()-1);
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> solution;
        process(solution, 1, k, n);
        return solutions;
    }
};
