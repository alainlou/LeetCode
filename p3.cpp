#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_map<char, int> seen;
        for(int j = 0, i = 0; j < s.size(); ++j) {
            if(seen.find(s[j]) != seen.end()) {
                i = max(seen[s[j]]+1, i);
            }
            ans = max(ans, j-i+1);
            seen[s[j]] = j;
        }
        return ans;
    }
};