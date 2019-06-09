#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size() + 1;
        int m = word2.size() + 1;
        int result[n][m];
        memset(result, 0, sizeof(result));
        for(int i = 0; i < m; ++i) {
            result[0][i] = i;
        }
        for(int j = 0; j < n; ++j) {
            result[j][0] = j;
        }
        for(int k = 1; k < n; ++k) {
            for(int l = 1; l < m; ++l) {
                result[k][l] = min(result[k-1][l], result[k][l-1]) + 1;
                if(word1[k-1] == word2[l-1]) {
                    result[k][l] = min(result[k][l], result[k-1][l-1]);
                } else {
                    result[k][l] = min(result[k][l], result[k-1][l-1] + 1);
                }
            }
        }
        return result[n-1][m-1];
    }
};