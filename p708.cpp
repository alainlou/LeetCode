#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
        for(int i = 0; i < str.size(); ++i) {
            if(str[i] >= 'A' && str[i] <= 'Z') {
                str[i] -= 'A' - 'a';
            }
        }
        return str;
    }
};
