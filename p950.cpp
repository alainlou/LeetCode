#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        vector<int> sorted(n);
        bool counts[1000001];
        memset(counts, false, sizeof(counts));
        for(int i : deck) {
            counts[i] = true;
        }
        int pntr = 0;
        for(int i = 0; i < 1000001; ++i) {
            if(counts[i]) {
                sorted[pntr] = i;
                ++pntr;
            }
        }
        pntr = 0;
        vector<int> solution(n);
        for(int i = 0; i < n; ++i) {
            solution[i] = sorted[pntr];
            sorted.erase(sorted.begin()+pntr);
            if(sorted.size() == 0)
                break;
            pntr += 2;
            pntr %= sorted.size();
        }
        return solution;
    }
};
