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
    void generate(string s, int diff, vector<string>& result, int n) {
        if(diff < 0)
            return;
        if(s.size() == n) {
            if(valid(s)) {
                result.push_back(s);
            }
        } else {
            generate(s + "(", diff+1, result, n);
            generate(s + ")", diff-1, result, n);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        generate("", 0, answer, 2*n);
        return answer;
    }
};