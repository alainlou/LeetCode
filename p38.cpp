#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string result = "1";
        for(int i = 1; i < n; ++i) {
            string str = "";
            char curr_c = result[0];
            int count = 0;
            for(char c : result) {
                if(c != curr_c) {
                    str += to_string(count) + curr_c;
                    count = 1;
                    curr_c = c;
                }
                else {
                    ++count;
                }
            }
            str += to_string(count) + curr_c;
            result = str;
        }
        return result;
    }
};