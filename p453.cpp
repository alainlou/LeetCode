#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        int answer = 0;
        int small = INT_MAX;
        for(int n : nums) small = min(n, small);
        for(int n : nums) answer += n - small;
        return answer;
    }
};
