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
    void generate(string s, int open, int close, vector<string>& result, int n) {
        if(s.size() == 2*n) {
            result.push_back(s);
        } 
        if(open < n)
            generate(s + "(", open+1, close, result, n);
        if(close < open)
            generate(s + ")", open, close+1, result, n);
    }
    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        generate("", 0, 0, answer, n);
        return answer;
    }
};