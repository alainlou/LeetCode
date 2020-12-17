from collections import Counter
from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        c = Counter()
        ans = 0

        for num1 in A:
            for num2 in B:
                c[num1+num2] += 1

        for num1 in C:
            for num2 in D:
                if -(num1+num2) in c:
                    ans += c[-(num1+num2)]

        return ans
