from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        if sqrt(n) == int(sqrt(n)):
            return 1
        for i in range(1, int(sqrt(n))+1):
            if sqrt(n-i*i) == int(sqrt(n-i*i)):
                return 2
        while n%4 == 0:
            n //= 4
        if n%8 == 7:
            return 4
        return 3
