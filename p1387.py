from functools import lru_cache

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache(None)
        def steps(n):
            if n == 1:
                return 0
            elif n%2 == 0:
                return 1 + steps(n//2)
            else:
                return 1 + steps(3*n + 1)

        def compare(n1, n2):
            val1 = steps(n1)
            val2 = steps(n2)

            if val1 == val2:
                return -1 if n1 < n2 else 1
            elif val1 < val2:
                return -1
            else:
                return 1

        arr = [i for i in range(lo, hi + 1)]

        arr.sort(key = cmp_to_key(compare))

        return arr[k-1]
