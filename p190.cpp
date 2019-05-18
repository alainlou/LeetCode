#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for(int i = 0; i < 31; ++i) {
            result += (n&1);
            n >>= 1;
            result <<= 1;
        }
        result += (n&1);
        return result;
    }
};