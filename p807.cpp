#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> h_skyline(n, 0);
        vector<int> v_skyline(n, 0);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                h_skyline[i] = max(h_skyline[i], grid[i][j]);
                v_skyline[j] = max(v_skyline[j], grid[i][j]);
            }
        }
        int answer = 0;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                answer += min(h_skyline[i], v_skyline[j]) - grid[i][j];
            }
        }
        return answer;
    }
};
