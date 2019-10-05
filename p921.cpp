#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minAddToMakeValid(string S) {
        int count = 0;
        int balance = 0;
        for(char c : S) {
            if(c == '(')
                ++balance;
            else
                --balance;
            if(balance < 0) {
                ++count;
                balance = 0;
            }
        }
        return count + balance;
    }
};
