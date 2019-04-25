#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int counter = 0;
        for(int i {5}; n/i > 0; i *= 5) {
            counter += n/i;
            if(i > INT_MAX/5) {
                break;
            }
        }
        return counter;
    }
};