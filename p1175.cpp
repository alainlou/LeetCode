#include <bits/stdc++.h>

using namespace std;

class Solution {
public:    
    unsigned long long mod = pow(10, 9) + 7;    
    unsigned long long factorial(int n) {
        if(n == 0 || n == 1)
            return 1;
        return n*factorial(n-1)%mod;
    }
    int numPrimeArrangements(int n) {
        bool isprime[101];        
        memset(isprime, true, sizeof(isprime));
        isprime[0] = false;
        isprime[1] = false;
        isprime[2] = true;
        for(int i = 3; i < 101; ++i) {
            for(int j = i-1; j >= 2; --j) {
                if(i%j == 0) {
                    isprime[i] = false;
                    break;
                }
            }
        }
        int num_primes = 0;
        for(int i = 0; i <= n; ++i) {
            if(isprime[i])
                ++num_primes;
        }
        return (factorial(n-num_primes) * factorial(num_primes))%mod;
    }
};
