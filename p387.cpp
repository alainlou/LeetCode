#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> exists;
        for(char c : s) {
            ++exists[c];
        }
        for(int i {0}; i < s.size(); ++i){
            if(exists[s[i]] == 1){
                return i;
            }
        }
        return -1;
    }
};