#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = s.size() > 0 && s[0] != ' ';
        for(int i = 1; i < s.size(); ++i) {
            if(s[i-1] == ' ' && s[i] != ' ')
                count = 1;
            else if(s[i] == ' ')
                continue;
            else
                ++count;
        }
        return count;
    }
};
