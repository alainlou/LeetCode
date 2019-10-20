#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int balancedString(string s) {
        int Q = 0;
        int W = 0;
        int E = 0;
        int R = 0;
        for(char c : s) {
            if(c == 'Q')
                ++Q;
            else if(c == 'W')
                ++W;
            else if(c == 'E')
                ++E;
            else
                ++R;
        }
        int n = Q + W + E + R;
        int d = n/4;
        int Qd = Q-d;
        int Wd = W-d;
        int Ed = E-d;
        int Rd = R-d;
        // check first
        if(Qd == 0 && Wd == 0 && Ed == 0 && Rd == 0)
            return 0;
        // get enough of the positives
        int left = 0;
        int right = 0;
        int answer = INT_MAX;
        char c = s[right];
        if(c == 'Q')
            --Qd;
        else if(c == 'W')
            --Wd;
        else if(c == 'E')
            --Ed;
        else
            --Rd;
        // two pointers algorithm
        while(left < s.size() && right < s.size()) {
            if(Qd <= 0 && Wd <= 0 && Ed <= 0 && Rd <= 0) {
                answer = min(answer, right-left+1);
                char c = s[left];
                if(c == 'Q')
                    ++Qd;
                else if(c == 'W')
                    ++Wd;
                else if(c == 'E')
                    ++Ed;
                else
                    ++Rd;
                ++left;                
            } else {
                ++right;
                char c = s[right];
                if(c == 'Q')
                    --Qd;
                else if(c == 'W')
                    --Wd;
                else if(c == 'E')
                    --Ed;
                else
                    --Rd;
            }
        }
        return answer;
    }
};
