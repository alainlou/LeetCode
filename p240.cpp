#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool search(vector<vector<int>> &matrix, int left, int right, int top, int bottom, int target) {
        // check in bound (if not then the step before couldn't find it)
        if(left > right || top > bottom)
            return false;
        // if the number is not in our range we can immediately stop searching
        else if(target > matrix[bottom][right] || target < matrix[top][left])
            return false;
        int x_mid = (right+left)/2;
        int y_mid = (top+bottom)/2;
        if(matrix[y_mid][x_mid] == target) {
            return true;
        } else if(matrix[y_mid][x_mid] > target) {
            // don't search squares we know are greater
            // squares that are less than our point for sure -> top-left            
            // squares that we don't know if they are less -> top-right and bottom-left
            bool possible_1 = search(matrix, left, right, top, y_mid-1, target);
            bool possible_2 = search(matrix, left, x_mid-1, y_mid, bottom, target);
            return possible_1 || possible_2;
        } else {
            bool possible_1 = search(matrix, left, right, y_mid+1, bottom, target);
            bool possible_2 = search(matrix, x_mid+1, right, top, y_mid, target);
            return possible_1 || possible_2;
        }
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0 || matrix[0].size() == 0) {
            return false;
        }
        return search(matrix, 0, matrix[0].size()-1, 0, matrix.size()-1, target);
    }
};