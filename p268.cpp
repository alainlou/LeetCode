#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int answer = 0;
        for(int i {0}; i < nums.size(); ++i){
            answer += i+1;
            answer -= nums[i];
        }
        return answer;
    }
};