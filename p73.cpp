#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> rows = {};
        vector<int> columns = {};
        
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = 0; j < matrix[0].size(); ++j){
                if(matrix[i][j] == 0){
                    rows.push_back(i);
                    columns.push_back(j);
                }
            }
        }

        for(int row : rows){
            for(int col = 0; col < matrix[0].size(); ++col){
                matrix[row][col] = 0;
            }
        }

        for(int col : columns){
            for(int row = 0; row < matrix.size(); ++row){
                matrix[row][col] = 0;
            }
        }
        
    }
};