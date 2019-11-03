#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        vector<bool> result;
        int n = s.size();
        int counts[n][26];
        memset(counts, 0, sizeof(counts));
        counts[0][s[0]-'a'] = 1;
        for(int i = 1; i < n; ++i) {
            for(int j = 0; j < 26; ++j) {
                counts[i][j] = counts[i-1][j];
            }
            ++counts[i][s[i]-'a'];
        }
        for(vector<int> q : queries) {
            int left = q[0];
            int right = q[1];
            int k = q[2];
            int len = right-left+1;            
            int num_odd = 0;
            if(left == 0) {
                for(int i = 0; i < 26; ++i) {
                    if(counts[right][i]%2 == 1)
                        ++num_odd;
                } 
            } else {
                for(int i = 0; i < 26; ++i) {
                    if((counts[right][i]-counts[left-1][i])%2 == 1)
                        ++num_odd;
                }                
            }            
            if(len%2 == 1)
                result.push_back(num_odd-1 <= 2*k);
            else
                result.push_back(num_odd <= 2*k);
        }
        return result;        
    }
};
