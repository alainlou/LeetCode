#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int counter = 0;
        int n = A.size();
        int m = B.size();
        int o = C.size();
        int p = D.size();
        map<int, int> counts;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                ++counts[A[i]+B[j]];
            }
        }
        for(int k = 0; k < o; ++k) {
            for(int l = 0; l < p; ++l) {
                counter += counts[-(C[k]+D[l])];
            }
        }
        return counter;
    }
};