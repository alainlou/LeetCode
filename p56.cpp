#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.size() == 0) {
            return intervals;
        }
        sort(intervals.begin(), intervals.end());
        for(int i = 0; i < intervals.size() - 1; ++i) {
            if(intervals[i+1][0] <= intervals[i][1]) {
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1]);
                intervals.erase(intervals.begin() + i + 1);
                --i;
            }
        }
        return intervals;
    }
};