#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool valid(string s) {
        int diff = 0;
        for(char c : s) {
            if(c == '(')
                ++diff;
            else
                --diff;
            if(diff < 0)
                return false;
        }
        return diff == 0;
    }
    void generate(string s, vector<string>& result, int n) {
        if(s.size() == n) {
            if(valid(s)) {
                result.push_back(s);
            }
        } else {
            generate(s + "(", result, n);
            generate(s + ")", result, n);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        generate("", answer, 2*n);
        return answer;
    }
};