#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool palindrome(string s, int start, int end) {
        for(int i = 0; i < (end-start)/2 + 1; ++i) {
            if(s[start+i] != s[end-i])
                return false;
        }
        return true;
    }
    int countSubstrings(string s) {
        int n = s.size();
        int count = n;
        // generating all substrings and checking if they're palindromes
        for(int i = 0; i < n; ++i) {
            for(int j = i+1; j < n; ++j) {
                // add one if it is a valid palindrome
                count += palindrome(s, i, j);
            }
        }
        return count;
    }
};