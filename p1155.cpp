#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    map<tuple<int, int, int>, int> solutions;
    int numRollsToTarget(int d, int f, int target) {
        if(solutions.find({d, f, target}) != solutions.end()) {
            return solutions[{d, f, target}];
        }
        if(d == 1) {
            return target <= f;
        }
        long long result = 0;
        for(int i = 1; i <= f; ++i) {
            if(target-i >= (d-1)) {
                int roll = numRollsToTarget(d-1, f, target-i);
                result += roll;
            }  
        }
        solutions[{d, f, target}] = result % int(pow(10, 9)+7);
        return result % int(pow(10, 9)+7);
    }
};
