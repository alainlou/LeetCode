from collections import defaultdict

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        matches = defaultdict(int)

        for p in pairs:
            matches[p[0]] = p[1]
            matches[p[1]] = p[0]

        ans = 0

        for i, p in enumerate(preferences):
            for e in p:
                if e == matches[i]:
                    break
                if preferences[e].index(i) < preferences[e].index(matches[e]):
                    ans += 1
                    break

        return ans
