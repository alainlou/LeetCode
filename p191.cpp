#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int result = 0;
        unsigned int bit = 1;
        for(int i = 0; i < 32; i++) {
            if((bit&n) != 0) {
                ++result;
            }
            bit <<= 1;
        }
        return result;
    }
};