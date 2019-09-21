#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        int n = mat.size();
        int pntrs[n];
        memset(pntrs, 0, sizeof(pntrs));
        while(true) {
            int maximum = 0;
            for(int i = 0; i < n; ++i) {
                maximum = max(maximum, mat[i][pntrs[i]]);
            }
            for(int i = 0; i < n; ++i) {
                while(mat[i][pntrs[i]] < maximum) {
                    if(pntrs[i] >= mat[0].size()-1)
                        return -1;
                    ++pntrs[i];
                }
            }
            // check if they are equal
            bool flag = true;
            for(int i = 0; i < n; ++i) {
                if(mat[i][pntrs[i]] != maximum) {
                    flag = false;
                    break;
                }
            }
            if(flag)
                return maximum;
        }        
    }
};
