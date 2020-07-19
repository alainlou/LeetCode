class Solution:
    def myPow(self, x: float, n: int) -> float:
        @lru_cache(None)
        def solve(n):
            if n == 0:
                return 1
            if n < 0:
                return 1/solve(-n)
            if n == 1:
                return x
            elif n%2 == 0:
                return solve(n//2)*solve(n//2)
            return solve(n//2)*solve(n//2+1)
        return solve(n)
