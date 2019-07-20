#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> solution;
        for(int i = 0; i <= num; ++i) {
            int curr = 0;
            int tmp = i;
            while(tmp != 0) {
                curr += tmp%2;
                tmp >>= 1;
            }
            solution.push_back(curr);
        }
        return solution;
    }
};