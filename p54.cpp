#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.size() == 0) {
            return {};
        }
        int m = matrix.size();
        int n = matrix[0].size();
        bool visited[m][n];
        memset(visited, false, sizeof(visited));
        vector<int> result = {};
        int direction = 0;
        int y = 0;
        int x = 0;
        while(result.size() < m*n) {
            result.push_back(matrix[y][x]);
            visited[y][x] = true;
            if(direction == 0) {
                if(x+1 < n && !visited[y][x+1]) {
                    ++x;
                }
                else {
                    direction = (direction+1)%4;
                    ++y;
                }
            } else if(direction == 1) {
                if(y+1 < m && !visited[y+1][x]) {
                    ++y;
                }
                else {
                    direction = (direction+1)%4;
                    --x;
                }
            } else if(direction == 2) {
                if(x-1 >= 0 && !visited[y][x-1]) {
                    --x;
                }
                else {
                    direction = (direction+1)%4;
                    --y;
                }
            } else {
                if(y-1 >= 0  && !visited[y-1][x]) {
                    --y;
                }
                else {
                    direction = (direction+1)%4;
                    ++x;
                }
            }
        }
        return result;
    }
};