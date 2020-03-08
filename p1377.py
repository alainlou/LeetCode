from functools import lru_cache

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        connected = {i:set() for i in range(1, n+1)}

        for e in edges:
            connected[e[0]].add(e[1])
            connected[e[1]].add(e[0])

        @lru_cache(None)
        def recurse(curr, t, bitmask):

            bitmask += 1 << curr

            if t == 0:
                return curr == target

            others = set()

            for c in connected[curr]:
                if (1 << c) & (bitmask) == 0:
                    others.add(c)

            n = len(others)
            if n == 0:
                return curr == target

            ans = 0
            for node in others:
                ans += 1/n * recurse(node, t-1, bitmask)

            bitmask -= 1 << curr

            return ans

        return recurse(1, t, 0)
