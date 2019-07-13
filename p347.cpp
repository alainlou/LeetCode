#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    static bool comp(pair<int, int> p1, pair<int, int> p2) {
        return p1.second > p2.second;
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for(int n : nums) {
            ++counts[n];
        }
        vector<pair<int, int>> arr;
        for(auto iter = counts.begin(); iter != counts.end(); ++iter) {
            arr.push_back({iter->first, iter->second});
        }
        sort(arr.begin(), arr.end(), comp);
        vector<int> result;
        for(int i = 0; i < k; ++i) {
            result.push_back(arr[i].first);
        }
        return result;
    }
};