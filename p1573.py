from math import factorial

class Solution:
    def numWays(self, s: str) -> int:
        mod = 10**9 + 7

        n = s.count('1')

        if n == 0:
            return (factorial(len(s)-1)//factorial(2)//factorial(len(s)-3))%mod # n-1 choose 2

        if n%3 != 0:
            return 0

        interval1, interval2 = 0, 0

        countdown = n

        for c in s:
            if c == '1':
                countdown -= 1
            if countdown == n//3*2:
                interval1 += 1
            if countdown == n//3:
                interval2 += 1

        return (interval1*interval2)%mod
