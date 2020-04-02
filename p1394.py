from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = defaultdict(int)

        for e in arr:
            counts[e] += 1

        ans = -1
        maximum = 0

        for c in counts:
            if c == counts[c] and counts[c] > ans and c > maximum:
                maximum = c
                ans = counts[c]

        return ans
