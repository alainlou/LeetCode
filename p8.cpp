#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        unsigned int answer = 0;
        unsigned int i = 0;
        bool negative = false;
        while(str[i] == ' ') {
            ++i;
        }
        if(str[i] == '-') {
            negative = true;
            ++i;
        } else if (str[i] == '+') {
            ++i;
        } 
        while('0' <= str[i] && str[i] <= '9') {
            if(INT_MAX/10 < answer)
                return negative ? INT_MIN : INT_MAX;
            answer *= 10;
            answer += str[i] - '0';
            ++i;
        }
        return negative ? -min(answer, (unsigned int)INT_MIN) : min(answer, (unsigned int)INT_MAX);
    }
};