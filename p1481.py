from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = defaultdict(int)
        for n in arr:
            counts[n] += 1
        a = []
        for v in counts.values():
            a.append(v)
        a.sort()
        while len(a) > 0 and k >= a[0]:
            k -= a[0]
            del a[0]


        return len(a)
