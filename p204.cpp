#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        if(n <= 2) return 0;
        bool* isPrime = new bool[n];
        memset(isPrime, true, sizeof(bool)*n);
        isPrime[0] = false;
        isPrime[1] = false;
        isPrime[2] = true;
        for(int i {0}; i < sqrt(n); ++i) {
            if(isPrime[i]) {
                for(int j {i*i}; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        int count = 0;
        for(int k = 0; k < n; ++k) {
            if(isPrime[k])
                ++count;
        }
        return count;
    }
};