#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    static bool compare(string str1, string str2) {
        if(str1.substr(str1.find(" ")) == str2.substr(str2.find(" "))) {
            return str1 < str2;
        } else {
            return str1.substr(str1.find(" ")) < str2.substr(str2.find(" "));
        }
    }
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> digit_logs;
        vector<string> letter_logs;
        for(string log : logs) {
            if(log[log.find(" ") + 1] >= '0' && log[log.find(" ") + 1] <= '9') {
                digit_logs.push_back(log);
            } else {
                letter_logs.push_back(log);
            }
        }
        sort(letter_logs.begin(), letter_logs.end(), compare);
        letter_logs.insert(letter_logs.end(), digit_logs.begin(), digit_logs.end());
        return letter_logs;
    }
};