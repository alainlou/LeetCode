#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findIntersection(vector<int> one, vector<int> two) {
        if(one[0] > two[1])
            return {-1};
        else if(two[0] > one[1])
            return {-2};
        else
            return {max(one[0], two[0]), min(one[1], two[1])};
    }
    vector<int> minAvailableDuration(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
        sort(slots1.begin(), slots1.end());
        sort(slots2.begin(), slots2.end());
        int pntr1 = 0;
        int pntr2 = 0;
        while(pntr1 < slots1.size() && pntr2 < slots2.size()) {
            // find if they are intersecting
            vector<int> intersection = findIntersection(slots1[pntr1], slots2[pntr2]);
            if(intersection.size() == 2 && intersection[1]-intersection[0] >= duration) {
                return {intersection[0], intersection[0]+duration};
            } else if(intersection[0] == -1) {
                ++pntr2;
            } else {
                ++pntr1;
            }
        }
        return {};
    }
};
