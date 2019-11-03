#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int n = s.size();
        vector<int> costs(n, 0);
        for(int i = 0; i < n; ++i) {
            costs[i] = abs(s[i]-t[i]);
        }
        int answer = 0;
        int cost = costs[0];
        int left = 0;
        int right = 0;
        while(left < n && right < n) {
            while(cost <= maxCost && right < n) {
                answer = max(answer, right-left+1);
                ++right;
                if(right >= n) break;
                cost += costs[right];
            }
            while(cost > maxCost && left < n) {
                cost -= costs[left];
                ++left;
            } 
        }
        return answer;
    }
};
