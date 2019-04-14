#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        digits[digits.size() - 1] += 1;
        if(digits[digits.size() - 1] == 10){
            bool carry = true;
            digits[digits.size() - 1] = 0;
            for(int i = digits.size()-2; i >= 0; i--){
                if(!carry){
                    break;
                }
                digits[i] += 1;
                if(digits[i] == 10){
                    digits[i] = 0;
                    carry = true;
                }
                else {
                    carry = false;
                }
            }
            if(carry){
                vector<int> copy = {1}; //insert at front
                for(int i : digits){
                    copy.push_back(i);
                }
                return copy;
            }
        }
        return digits;
    }
};