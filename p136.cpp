#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int> count;
        for(int num : nums) {
            ++count[num];
        }
        for(auto i = count.begin(); i != count.end(); ++i) {
            if(i->second == 1) {
                return i->first;
            }
        }
        return 0;
    }
};