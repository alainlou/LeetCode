#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minSquares[10000];
    int findMinSquares(int num) {
        if(minSquares[num] != 0) {
            return minSquares[num];
        } else if(num == 0) {
            return 0;
        } else if(num == 1) {
            return 1;
        } else {
            int min_count = INT_MAX;
            int curr_count = 0;
            for(int i = 1; i <= int(sqrt(num)); ++i) {
                int count = 1 + findMinSquares(num - i*i);
                if(count < min_count) {
                    min_count = count;
                }
            }
            minSquares[num] = min_count;
            return min_count;
        }
    }
    int numSquares(int n) {
        memset(minSquares, sizeof(minSquares), 0);
        return findMinSquares(n);
    }
};