#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        int n = puzzles.size();
        unordered_map<int, int> counts;
        for(string word : words) {
            int mask = 0;
            for(char c : word) {
                mask = mask|((int)pow(2, c-'a'));
            }
            ++counts[mask];
        }
        vector<int> solution(n, 0);
        for(int i = 0; i < n; ++i) {
            int mask = 0;
            for(char c : puzzles[i]) {
                mask = mask|((int)pow(2, c-'a'));
            }
            for(int submask = mask; submask > 0; submask = (submask-1) & mask) {
                if((submask&(int)pow(2,puzzles[i][0]-'a')) > 0 && 
                    counts.find(submask) != counts.end()) {
                    solution[i] += counts[submask];
                }
            }
        }
        return solution;
    }
};
