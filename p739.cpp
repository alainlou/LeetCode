#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> result(T.size(), 0);
        stack<pair<int, int>> s;
        s.push({T[0], 0});
        for(int i = 1; i < T.size(); ++i) {
            while(!s.empty() && T[i] > s.top().first) {
                result[s.top().second] = i-s.top().second;
                s.pop();
            }
            s.push({T[i], i});
        }
        result[T.size()-1] = 0;
        return result;
    }
};