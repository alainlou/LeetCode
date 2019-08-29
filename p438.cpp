#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int len = p.size();
        int count[26];
        int mask[26];
        memset(count, 0, sizeof(count));
        memset(mask, 0, sizeof(mask));
        for(char c : p) {
            ++count[c-'a'];
        }
        // fill
        for(int i = 0; i < min(s.size(), p.size()); ++i) {
            ++mask[s[i]-'a'];
        }
        // result
        vector<int> result;
        bool match = true;
        for(int j = 0; j < 26; ++j) {
            if(count[j] != mask[j])
                match = false;
        }
        if(match)
            result.push_back(0);
        // check
        for(int i = len; i < s.size(); ++i) {
            ++mask[s[i]-'a'];
            --mask[s[i-len]-'a'];
            bool match = true;
            for(int j = 0; j < 26; ++j) {
                if(count[j] != mask[j])
                    match = false;
            }
            if(match)
                result.push_back(i+1-len);
        }
        return result;
    }
};
