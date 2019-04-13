#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int answer = 0;
        map<string, int> table = {
            {"M", 1000},
            {"CM", 900},
            {"D", 500},
            {"CD", 400},
            {"C", 100},
            {"XC", 90},
            {"L", 50},
            {"XL", 40},
            {"X", 10},
            {"IX", 9},
            {"V", 5},
            {"IV", 4},
            {"I", 1}
        };
        
        for(int i = 0; i < s.size(); ++i){
            if(i < s.size() - 1 && table[s.substr(i, 2)]){
                answer += table[s.substr(i,2)];
                ++i;
            }
            else{
                answer += table[s.substr(i,1)];
            }
        }
        
        return answer;
    }
};