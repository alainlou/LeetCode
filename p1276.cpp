#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        if(cheeseSlices > 0 && tomatoSlices/cheeseSlices < 2)
            return {};
        vector<int> tmp = {0,0};
        while(tomatoSlices > 3 && cheeseSlices > 0 && (double)tomatoSlices/cheeseSlices > 2){
            tomatoSlices -= 4;
            cheeseSlices -= 1;
            ++tmp[0];
        }
        if(cheeseSlices == 0)
            return tomatoSlices == 0 ? tmp : vector<int>();
        else if((double)tomatoSlices/cheeseSlices == 2) {
            tmp[1] = cheeseSlices;
            return tmp;
        }            
        return {};
    }
};