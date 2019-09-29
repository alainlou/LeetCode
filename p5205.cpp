#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        int occur[2001];
        memset(occur, 0, sizeof(occur));
        for(int i : arr) {
            ++occur[i+1000];
        }
        sort(begin(occur), end(occur));
        for(int i = 0; i < 2000; ++i) {
            if(occur[i] != 0 && occur[i] == occur[i+1])
                return false;
        }
        return true;
    }
};
