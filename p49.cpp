#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> result;
        for(string s : strs) {
            array<int, 26> count;
            memset(count.begin(), 0, sizeof(count));
            for(char c : s) {
                ++count[c-'a'];
            }
            if(result.find(count) != result.end()) {
                result[count].push_back(s);
            } else {
                result[count] = {s};
            }
        }
        vector<vector<string>> answer;
        for(auto i = result.begin(); i != result.end(); ++i) {
            answer.push_back(i->second);
        }
        return answer;
    }
};