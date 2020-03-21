from collections import defaultdict

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        counts = defaultdict(int)

        for e in arr1:
            counts[e] += 1

        for e in arr2:
            for i in range(e-d, e+d+1):
                counts[i] = 0

        return sum(counts.values())
