#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1)
            return s;
        vector<string> result(numRows);
        int row = 0;
        bool down = true;
        for(char c : s) {
            result[row] += c;
            if(row == numRows-1) {
                down = false;
                --row;
            } else if(row == 0) {
                down = true;
                ++row;
            } else if(down) {
                ++row;
            } else {
                --row;
            }
        }
        string answer = "";
        for(string s : result) {
            answer += s;
        }
        return answer;
    }
};