#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        set<char> s;
        for(char c : J) {
            s.insert(c);
        }
        int count = 0;
        for(char c : S) {
            if(s.find(c) != s.end()) {
                ++count;
            }
        }
        return count;
    }
};