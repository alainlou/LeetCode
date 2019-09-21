#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxNumberOfApples(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int carry = 0;
        int count = 0;
        for(int a : arr) {
            if(carry > 5000) {
                break;
            }
            carry += a;
            ++count;
        }
        if(carry > 5000) {
            --count;
        }
        return count;
    }
};
