#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        int steps[n];
        memset(steps, 0, sizeof(steps));
        steps[0] = 1;
        if(n > 1)
            steps[1] = 1;
        for(int i = 0; i < n - 2; ++i) {
            steps[i+1] += steps[i];
            steps[i+2] += steps[i];
        }
        if(n > 1)
            steps[n-1] += steps[n-2];
        return steps[n-1];
    }
};