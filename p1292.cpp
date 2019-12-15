#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int n = mat.size();
        int m = mat[0].size();
        int ans = 0;
        
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                int s = 0;
                int l = 0;
                bool flag = false;
                while(s < threshold && i+l < n && j+l < m) {
                    for(int k = 0; k < l; ++k) {
                        s += mat[i+l][j+k];
                        s += mat[i+k][j+l];
                    }
                    s += mat[i+l][j+l];
                    if(s > threshold) {
                        break;
                    }
                    ++l;
                }
                ans = max(ans, l);
            }
        }
        return ans;
    }
};