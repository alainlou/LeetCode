#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        double xd0 = coordinates[1][0] - coordinates[0][0];
        double yd0 = coordinates[1][1] - coordinates[0][1];
        double slope0 = yd0/xd0;
        for(int i = 2; i < coordinates.size(); ++i) {
            double xd = coordinates[i][0] - coordinates[i-1][0];
            double yd1 = coordinates[i][1] - coordinates[i-1][1];
            double slope = yd1/xd;
            if(slope != slope0)
                return false;
        }
        return true;
    }
};
