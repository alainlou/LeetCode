#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for(char c : s) {
            result *= 26;
            result += c - 64;
        }
        return result;
    }
};