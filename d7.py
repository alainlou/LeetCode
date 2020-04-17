from collections import defaultdict

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0

        for a in arr:
            counts[a] += 1

        for a in arr:
            ans += 1 if a+1 in counts else 0

        return ans
