#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string alphaNumeric(string s) {
        string result = "";
        for(char chr : s) {
            chr = tolower(chr);
            if((chr > 96 && chr < 123)
               || (chr > 47 && chr < 58)) {
                result += chr;
            }
        }
        return result;
    }
    bool isPalindrome(string s) {
        s = alphaNumeric(s);
        int n = s.size();
        for(int i = 0; i < n; ++i) {
            if(s[i] != s[n-i-1]) {
                return false;
            }
        }
        return true;
    }
};