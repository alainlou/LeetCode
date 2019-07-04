#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool binary_search(vector<int> &vec, int target, int start, int end) {
        if(target < vec[start] || target > vec[end])
            return false;
        int mid = (end+start)/2;
        if(vec[mid] == target)
            return true;
        else if(vec[mid] > target)
            return binary_search(vec, target, start, mid-1);
        else
            return binary_search(vec, target, mid+1, end);
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0 || matrix[0].size() == 0)
            return false;
        int m = matrix.size();
        int n = matrix[0].size();
        // find the row that contains our number
        for(int i = 0; i < m; ++i) {
            // we found the row
            if(matrix[i][0] <= target && matrix[i][n-1] >= target) {
                // binary search on the row
                return binary_search(matrix[i], target, 0, n-1);
            }
        }
        // it's out of range of all of our rows
        return false;
    }
};