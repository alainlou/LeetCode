from functools import lru_cache

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        @lru_cache(None)
        def divisors(n):
            if n == 1:
                return {1}
            s = {1, n}
            for i in range(2, int(sqrt(n))+1):
                if n%i == 0:
                    s |= divisors(i)
                    s |= divisors(n//i)
            return s

        for n in nums:
            divs = divisors(n)
            if len(divs) == 4:
                ans += sum(divs)

        return ans
