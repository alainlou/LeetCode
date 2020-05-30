from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)

        for a in target:
            counts1[a] += 1
        for b in arr:
            counts2[b] += 1

        for k, v in counts1.items():
            if counts2[k] != v:
                return False

        return True
