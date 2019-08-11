#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<string> split(string s, string delim) {
        vector<string> answer;
        
        size_t last = 0;
        size_t next = 0;
        
        while((next = s.find(delim, last)) != string::npos) {
            answer.push_back(s.substr(last, next-last));
            last = next + 1;
        }
        answer.push_back(s.substr(last));
        
        return answer;
    }
    int dayOfYear(string date) {
        int answer = 0;
        vector<string> d = split(date, "-");
        bool is_leap = false;
        int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        int year = stoi(d[0]);
        
        if(year%4 == 0 && year%100 != 0)
            is_leap = true;
        
        for(int i = 1; i < stoi(d[1]); ++i) {
            if(i == 2 && is_leap)
                answer += 1;
            answer += days[i];
        }
        
        answer += stoi(d[2]);
        
        return answer;
    }
};
