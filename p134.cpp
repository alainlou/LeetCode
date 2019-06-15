#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int curr = 0;
        for(int start = 0; start < n; ++start) {
            int curr_gas = 0;
            bool flag = true;
            curr = 0;
            while(curr < n + 1) {
                curr_gas += gas[(start+curr)%n];
                curr_gas -= cost[(start+curr)%n];
                 if(curr_gas < 0) {
                    flag = false;
                    break;
                }
                ++curr;
            }
            if(flag)
                return start;
        }
        return -1;
    }
};