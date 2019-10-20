#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        double xd = coordinates[1][0] - coordinates[0][0];
        double yd = coordinates[1][1] - coordinates[0][1];
        double slope = yd/xd;
        for(int i = 2; i < coordinates.size(); ++i) {
            double xd1 = coordinates[i][0] - coordinates[i-1][0];
            double yd1 = coordinates[i][1] - coordinates[i-1][1];
            double slope1 = yd1/xd1;
            if(slope1 != slope)
                return false;
        }
        return true;
    }
};
