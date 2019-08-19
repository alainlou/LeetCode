#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void fill(vector<vector<int>>& distances, int x, int y) {
        // fill the row
        vector<int> changed;
        for(int i = 0; i < distances[0].size(); ++i) {
            if(abs(i-y) < distances[x][i]) {
                distances[x][i] = abs(i-y);
                changed.push_back(i);
            }        
        }
        
        if(changed.size() == 0)
            return;
        
        // go up
        for(int i = x-1; i >= 0; --i) {
            for(int j : changed) {
                distances[i][j] = min(distances[i][j], distances[i+1][j] + 1);
            }
        }
        
        // go down
        for(int i = x+1; i < distances.size(); ++i) {
            for(int j : changed) {
                distances[i][j] = min(distances[i][j], distances[i-1][j] + 1);
            }
        }
    }
    int maxDistance(vector<vector<int>>& grid) {
        vector<vector<int>> distances(grid.size(), vector<int>(grid[0].size(), INT_MAX));
        bool has_land = false;
        bool has_water = false;
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid[0].size(); ++j) {
                if(grid[i][j] == 1) {
                    has_land = true;
                    fill(distances, i, j);
                } else {
                    has_water = true;
                }
            }
        }
        
        if(!has_land || !has_water)
            return -1;
        
        int answer = 0;
        for(int i = 0; i < distances.size(); ++i) {
            for(int j = 0; j < distances[0].size(); ++j) {
                answer = max(answer, distances[i][j]);
            }
        }
        return answer;
    }
};
