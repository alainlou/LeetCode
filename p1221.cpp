#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0;
        int result = 0;
        for(char c : s) {
            if(c == 'L') ++count;
            else --count;
            if(count == 0) ++result;
        }
        return result;
    }
};
