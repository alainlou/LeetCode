class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def recurse(n):
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)
            return recurse(sum([int(digit)**2 for digit in str(n)]))

        return recurse(n)
