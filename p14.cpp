#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int answer = 0;
        while(x != 0){
            int digit = x%10;
            x /= 10;
            if (answer > INT_MAX/10 || answer < INT_MIN/10)
                return 0;
            answer *= 10;
            answer += digit;
        }
        return answer;
    }
};