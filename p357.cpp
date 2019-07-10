#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int factorial(int n) {
        if(n == 1) {
            return 1;
        }
        return n * factorial(n-1);
    }
    int countNumbersWithUniqueDigits(int n) {
        // initialize with "0"
        int answer = 1;
        for(int i = 0; i < n; ++i) {
            answer += 9 * factorial(9)/factorial(9+i-(n-1));
        }
        return answer;
    }
};