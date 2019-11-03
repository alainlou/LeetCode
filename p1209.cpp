#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string removeDuplicates(string s, int k) {
        bool flag = false;
        char c = s[0];
        int count = 1;
        for(int i = 1; i < s.size(); ++i) {
            if(s[i] == c) {
                ++count;
                if(count == k) {
                    flag = true;
                    for(int j = 0; j < k; ++j) {
                        s.erase(s.begin()+i-k+1);
                    }
                    i = max(-1, i-5);
                    if(i >= s.size()) break;
                    c = s[i];
                    count = 1;
                }
            } else {
                c = s[i];
                count = 1;
            }
        }
        if(!flag) return s;
        return removeDuplicates(s, k);
    }
};
