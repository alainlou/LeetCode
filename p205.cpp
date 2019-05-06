#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.size() != t.size())
            return false;
        map<char, char> replacements;
        map<char, char> replace_back;
        for(int i = 0; i < s.size(); ++i) {
            if((replacements.count(s[i]) > 0 && replacements[s[i]] != t[i])
              || (replace_back.count(t[i]) > 0 && replace_back[t[i]] != s[i]))
                return false;
            replacements[s[i]] = t[i]; 
            replace_back[t[i]] = s[i];
        }
        return true;
    }
};