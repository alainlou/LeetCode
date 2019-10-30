#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isSelfDividing(int num) {
        int copy = num;
        while(copy != 0) {
            int digit = copy%10;
            if(digit == 0 || num%digit != 0)
                return false;
            copy /= 10;
        }
        return true;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> solution;
        for(int i = left; i <= right; ++i) {
            if(isSelfDividing(i))
                solution.push_back(i);
        }
        return solution;
    }
};