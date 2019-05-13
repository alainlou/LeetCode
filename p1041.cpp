#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isRobotBounded(string instructions) {
        pair<int, int> coordinates;
        int rotation = 0;
        for(char c : instructions) {
            if(c == 'L') {
                --rotation;
            } else if(c == 'R') {
                ++rotation;
            } else if(c == 'G') {
                while(rotation < 0) {
                    rotation += 4;
                }
                rotation = rotation % 4;
                switch(rotation) {
                    case 0 : ++coordinates.second;
                        break;
                    case 1 : ++coordinates.first;
                        break;
                    case 2 : --coordinates.second;
                        break;
                    case 3 : --coordinates.first;
                        break;
                }
            }
        }
        bool zero = coordinates.first == 0 && coordinates.second == 0;
        return (rotation != 0  && (!zero)) || (zero);
    }
};