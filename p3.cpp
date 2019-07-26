#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_set<char> seen;
        for(int i = 0; i < s.size(); ++i) {
            int curr = 0;
            unordered_set<char> seen;
            // create the longest substring at the starting index
            for(int j = i; j < s.size(); ++j) {
                // it has been seen
                if(seen.find(s[j]) != seen.end()) {
                    break;
                } else {
                    ++curr;
                    seen.insert(s[j]);
                }
            }
            ans = max(curr, ans);
        }
        return ans;
    }
};