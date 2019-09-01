#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        unsigned long long count = 0;        
        bool negative = dividend < 0 ^ divisor < 0;
        long long top = abs((long long)dividend);
        long long bottom = abs((long long)divisor);
        while(top >= 10000*bottom) {
            top -= 10000*bottom;
            count += 10000;
        }
        while(top >= bottom) {
            top -= bottom;
            ++count;
        }
        if(count > INT_MAX)
            return negative ? INT_MIN : INT_MAX;
        return negative ? -count : count;
    }
};
