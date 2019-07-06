#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    unordered_map<int, bool> solutions;
    bool works(vector<int>& weights, int D, int cap) {
        int i = 0;
        for(int day = 0; day < D; ++day) {
            int c = cap;
            while(i < weights.size() && weights[i] <= c) {
                c -= weights[i];
                ++i;
            }
        }
        return i == weights.size();
    }
    int shipWithinDays(vector<int>& weights, int D) {
        int lo = 0;
        int hi = 0;
        for(int w : weights) {
            hi += w;
        }
        while(true) {
            int capacity = (hi+lo)/2;
            bool curr = works(weights, D, capacity);
            bool prev = works(weights, D, capacity-1);
            if(!prev && curr)
                return capacity;
            else if(prev)
                hi = capacity-1;
            else
                lo = capacity+1;
        }
    }
};