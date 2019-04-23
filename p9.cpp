#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int num = x;
        int num_digits = int(log10(x)) + 1;
        int reverse = 0;
        for(int i {0}; i < num_digits; ++i) {
            if(reverse > INT_MAX/10) 
                return false;
            reverse = reverse*10 + x%10;
            x /= 10;
        }
        return reverse == num;
    }
};