#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        for(int i {0}; i < b; ++i){
            ++a;
        }
        for(int j {0}; j > b; --j){
            --a;
        }
        return a;
    }
};