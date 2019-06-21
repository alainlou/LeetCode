#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0) {
            return 0;
        }
        // this tells you the max number of cells on the left you can go filled with '1'
        vector<vector<int>> integral;
        for(int i = 0; i < matrix.size(); ++i) {
            vector<int> row;
            int carry = 0;
            for(int j = 0; j < matrix[0].size(); ++j) {
                if(matrix[i][j] == '0') {
                    carry = 0;
                } else {
                    ++carry;
                }
                row.insert(row.begin(), carry);
            }
            integral.push_back(row);
        }
        int max_area = 0;
        // compute the "maximum for each column" and update max_area
        for(int col = 0; col < integral[0].size(); ++col) {
            int max_width = 0;
            set<int> widths;
            for(int row = 0; row < integral.size(); ++row) {
                max_width = max(max_width, integral[row][col]);
                widths.insert(integral[row][col]);
            }
            // calculate rectangle for a given width through a col
            for(int width : widths) {
                int curr_area = 0;
                for(int row = 0; row < integral.size(); ++row) {
                    if(integral[row][col] >= width) {
                        curr_area += width;
                    } else {
                        curr_area = 0;
                    }
                    max_area = max(max_area, curr_area);
                }
            }
        }
        return max_area;
    }
};