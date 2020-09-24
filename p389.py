from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(c for c in s)

        for c in t:
            counts[c] -= 1
            if counts[c] == 0:
                del counts[c]

        return list(counts.keys())[0]
