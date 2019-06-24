#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int num1;
        int num2;
        int count1 = 0;
        int count2 = 0;
        for(int n : nums) {
            if(n == num1) {
                ++count1;
            } else if(n == num2) {
                ++count2;
            } else if(count1 == 0) {
                num1 = n;
                ++count1;
            } else if(count2 == 0) {
                num2 = n;
                ++count2;
            } else {
                --count1;
                --count2;
            }
        }
        int n = nums.size();
        int actual1 = 0;
        int actual2 = 0;
        for(int i : nums) {
            if(i == num1) {
                ++actual1;
            } else if(i == num2) {
                ++actual2;
            }
        }
        vector<int> result;
        if(actual1 > n/3)
            result.push_back(num1);
        if(actual2 > n/3)
            result.push_back(num2);
        return result;
    }
};