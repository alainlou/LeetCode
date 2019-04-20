#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0){
            return 0;
        }
        int profit = 0;
        int bought = prices[0];
        for(int i {1}; i < prices.size() - 1; ++i) {
            if(prices[i-1] >= prices[i] && prices[i+1] > prices[i]) {
                bought = prices[i];
            } else if(prices[i-1] < prices[i] && prices[i+1] <= prices[i]) {
                profit += prices[i] - bought;
            }
        }
        if(prices[prices.size() - 1] - bought > 0 &&
           prices[prices.size() - 1] > prices[prices.size() - 2]) {
            profit += prices[prices.size() - 1] - bought;
        }
        return profit;
    }
};