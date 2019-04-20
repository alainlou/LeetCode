#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
            return false;
        map<char, int> char_counts;
        for(char c : s) {
            ++char_counts[c];
        }
        for(char c : t) {
            if(char_counts.count(c) > 0 && char_counts[c] > 0)
                --char_counts[c];
            else
                return false;
        }
        return true;
    }
};