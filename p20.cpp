#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> open_brackets;
        for(int i {0}; i < s.size(); ++i) {
            switch(s[i]) {
                case ')':
                    if(open_brackets.empty() || open_brackets.top() != '(') return false;
                    open_brackets.pop();
                    break;
                case '}':
                    if(open_brackets.empty() || open_brackets.top() != '{') return false;
                    open_brackets.pop();
                    break;
                case ']':
                    if(open_brackets.empty() || open_brackets.top() != '[') return false;
                    open_brackets.pop();
                    break;
                default:
                    open_brackets.push(s[i]);
            }
        }
        return open_brackets.empty();
    }
};