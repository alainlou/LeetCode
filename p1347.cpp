#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minSteps(string s, string t) {
        vector<int> counts1(26, 0);
        vector<int> counts2(26, 0);

        for(char c : s) {
            counts1[c-'a']++;
        }

        for(char c : t) {
            counts2[c-'a']++;
        }

        int ans = 0;

        for(int i = 0; i < 26; ++i) {
            ans += abs(counts2[i]-counts1[i]);
        }

        return ans/2;
    }
};
