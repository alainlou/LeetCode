#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        int points = 0;
        int curr = 0;
        for(int i = 0; i < k; ++i) {
            curr += calories[i];
        }
        for(int i = k; i < calories.size(); ++i) {
            if(curr > upper) {
                ++points;
            } else if(curr < lower) {
                --points;
            }
            curr += calories[i];
            curr -= calories[i-k];
        }
         if(curr > upper) {
            ++points;
        } else if(curr < lower) {
            --points;
        }
        return points;        
    }
};
