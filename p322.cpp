#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int solutions[10000];
    int coinChange(vector<int>& coins, int amount) {
        memset(solutions, 0, sizeof(solutions));
        return solve(coins, amount);
    }
    int solve(vector<int> & coins, int amount) {
        if(amount < 0)
            return -1;
        else if(amount == 0)
            return 0;
        else if(solutions[amount] != 0)
            return solutions[amount];
        int solution = -1;
        for(int i = 0; i < coins.size(); ++i) {
            int result = solve(coins, amount - coins[i]);
            if(result > -1) {
                if(solution == -1) {
                    solution = result + 1;
                } else if(result < solution) {
                    solution = result + 1;
                }
            }
        }
        solutions[amount] = solution;
        return solution;
    }
};