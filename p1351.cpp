#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int ans = 0;
        
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid[0].size(); ++j) {
                ans += (grid[i][j] < 0);
            }
        }
        
        return ans;
    }
};