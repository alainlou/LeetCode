#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<string> result;
    map<char, string> num_to_letter = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"},
    };
    void generate(string s, string digits, int curr, int n) {
        if(s.size() == n) {
            result.push_back(s);
            return;
        }
        for(char c : num_to_letter[digits[curr]]) {
            generate(s+c, digits, curr+1, n);
        }
    }
    vector<string> letterCombinations(string digits) {
        int n = digits.size();
        if(n == 0)
            return result;
        generate("", digits, 0, n);
        return result;
    }
};