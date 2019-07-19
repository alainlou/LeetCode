#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void process(vector<vector<int>>& matrix, int i, int& n) {
        // top left is [i][i], top right is [i][n-1-i], bottom left is [n-1-i][i], bottom right is [n-1-i][n-1-i]
        for(int iter = i; iter < n-1-i; ++iter) {
            // store right
            int tmp = matrix[iter][n-1-i];
            // assign right
            matrix[iter][n-1-i] = matrix[i][iter];
            // assign top
            matrix[i][iter] = matrix[n-1-iter][i];
            // assign left
            matrix[n-1-iter][i] = matrix[n-1-i][n-1-iter];
            // assign bottom
            matrix[n-1-i][n-1-iter] = tmp;
        }
    }
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int i = 0; i < n/2; ++i) {
            process(matrix, i, n);
        }
    }
};