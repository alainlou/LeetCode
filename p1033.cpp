#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        vector<int> positions = {a, b, c};
        sort(positions.begin(), positions.end());
        int counter1 = 0;
        int diff1 = positions[1] - positions[0];
        int diff2 = positions[2] - positions[1];
        if(diff1 == 1 && diff2 == 1) {
            counter1 = 0;
        } else if(diff1 < 3 || diff2 < 3) {
            counter1 = 1;
        } else {
            counter1 = 2;
        }
        int counter2 = positions[1] - positions[0] + positions[2] - positions[1] - 2;
        return {counter1, counter2};
    }
};