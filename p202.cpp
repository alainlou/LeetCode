#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int sumDigitsSquared(int n) {
        int answer {0};
        while(n) {
            answer += pow(n%10, 2);
            n /= 10;
        }
        return answer;
    }
    bool isHappy(int n) {
        int slow {n};
        int fast {n};
        do {
            slow = sumDigitsSquared(slow);
            fast = sumDigitsSquared(sumDigitsSquared(fast));
        } while(slow != fast);
        if(slow == 1)
            return true;
        else
            return false;
    }
};