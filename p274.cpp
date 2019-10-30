#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        sort(citations.begin(), citations.end());
        for(int i = 0; i < n; ++i) {
            if(citations[n-1-i] < i+1)
                return i;
        }
        return n;
    }
};
