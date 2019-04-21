#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) 
            return "";
        size_t length = 0;
        size_t min_length = SIZE_MAX;
        for(string s : strs) {
            if(s.size() < min_length) {
                min_length = s.size();
            }
        }
        bool stop = false;
        for(size_t i {0}; i < min_length; ++i){
            char chr = strs[0][i];
            for(size_t j {1}; j < strs.size(); ++j) {
                if(strs[j][i] != chr) {
                    stop = true;
                }
            }
            if(stop) {
                break;
            }
            ++length;
        }
        return strs[0].substr(0, length);
    }
};