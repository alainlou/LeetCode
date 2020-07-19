from collections import defaultdict
from copy import copy
from functools import lru_cache

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        prelim = defaultdict(list)

        for i, c in enumerate(s):
            if c in prelim:
                prelim[c][1] = i
            else:
                prelim[c] = [i, i]

        rngs = copy(prelim)

        for r in rngs.values():
            while True:
                flag = False
                for i in range(r[0], r[1]+1):
                    if prelim[s[i]][0] < r[0]:
                        r[0] = prelim[s[i]][0]
                        flag = True
                    elif prelim[s[i]][1] > r[1]:
                        r[1] = prelim[s[i]][1]
                        flag = True
                if not flag:
                    break

        arr = list(sorted(rngs.values(), key=lambda x: x[0]))

        pick = [False]*len(arr)

        @lru_cache(None)
        def dfs(idx, avail):
            if idx > len(arr)-1:
                return 0
            ans = dfs(idx+1, avail)
            if arr[idx][0] >= avail:
                pick[idx] = True
                tmp = 1 + dfs(idx+1, arr[idx][1]+1)
                if tmp > ans:
                    ans = tmp
                else:
                    pick[idx] = False
            return ans

        dfs(0, 0)

        ans = []
        for i, p in enumerate(pick):
            if p:
                ans.append(s[arr[i][0]:arr[i][1]+1])

        return ans
