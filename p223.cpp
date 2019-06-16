#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int counter = 0;
        // set the bounds;
        int start_x = min(A, E);
        int n = max(C, G);
        int start_y = min(B, F);
        int m = max(D, H);
        for(int i = start_x; i < n; ++i) {
            for(int j = start_y; j < m; ++j) {
                // check if the block at the location is in the bounds;
                // case 1: it is in the first one
                if(i >= A && i+1 <= C && j >= B && j+1 <= D) {
                    ++counter;
                }
                // case 2: it is in the second one
                else if(i >= E && i+1 <= G && j >= F && j+1 <= H) {
                    ++counter;
                }
            }
        }
        return counter;
    }
};