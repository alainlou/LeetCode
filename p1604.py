from bisect import bisect_left
from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def translate(time):
            s = time.split(':')
            return 60*int(s[0]) + int(s[1])

        d = defaultdict(list)

        for i, k in enumerate(keyTime):
            t = translate(k)
            idx = bisect_left(d[keyName[i]], t)
            d[keyName[i]].insert(idx, t)

        ans = []

        for k, arr in d.items():
            for i in range(len(arr)-2):
                if arr[i+2]-arr[i] <= 60:
                    ans.append(k)
                    break

        ans.sort()

        return ans
